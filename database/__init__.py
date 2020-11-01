import random
from typing import List, Dict

import pandas as pd

from model import CategoryEnum, RecommendationTypeEnum, map_class
from model.places import Place
from model.profiles import Profile
from model.recommendations import Recommendation

# dummy profile
dummy_profile = Profile(
    '10', 'John Doe', 'https://i.pinimg.com/originals/c8/f7/a8/c8f7a86a5a668cac7a2846073ce4baf3.jpg', 20)

stories: List[str] = [
    'Kaava now works in limited mode ′′ windows ", but the e-commerce is still the same. We have a lot of new things for you, which will not only please, but also warm up not only outside, but also at home. A lot of strength and thank you all for your support!',
    'Cool, urban cafe with a selection of freshly-baked treats & a serious approach to its coffee. Our philosophy is simple, The pleasure of quality ingredients. Traditional techniques inspired by the latest technologies. Flashes of memories and non-traditional taste surprises. Love of craft, people and nature.',
    'We specialize in espresso bars and specialty coffee. Our philosophy is to keep things as simple as possible. Great things don’t need any additions. Come try our local roasts and enjoy a treat or two.',
    "Weekday farmers' market featuring locally sourced produce, flowers, handicrafts & food vendors. We are open rain or shine and provide the best local food. Come support your local farmers - and get fresh farm to table food! ",
    "We are a local sports helping you get the best equipment while providing exceptional service in the heart of Karlin for over 2 decades. We can get you any gear and match the “big corporate” prices! Come check us out get you started on your next sport adventure.",
    'The Biosophy Pure Beauty concept was created not only on the basis of the social demand for organic products, but above all as an expression of our long-term idea of ​​"pure beauty". Biosophy beauty concept store brings a unique combination of bio philosophy in the field of cosmetics sales and cosmetic care. Women can stop by us, refresh themselves and shop in peace, consul skin problems or products.',
]
photos: Dict[CategoryEnum, List[str]] = {
    CategoryEnum.coffee: [
        'https://i.pinimg.com/originals/ac/85/d7/ac85d7128f08d2b5fd15f34addb3be5e.jpg',
        'https://policygenius-blog.imgix.net/2018/08/coffee-house-crew.jpg'
    ],
    CategoryEnum.eating_out: [
        'https://www.telegraph.co.uk/content/dam/Travel/Destinations/Europe/Czech%20Republic/Prague/cafe-savoy-prague-intro.jpg',
        'https://www.prague-stay.com/images/lifestyle_article/270x200/0547-u-mg-5026-fit~u-zlate-konvice-prague-restaurant.jpg',
        'https://www.praguest.com/images//sampledata/restaurants/augustinerestaurant/Augustine-Restaurant-prague-interior2.jpg',
    ],
    CategoryEnum.party: [
        'https://www.barandbooks.cz/slider/tynska_40.jpg?1',
        'https://images.squarespace-cdn.com/content/v1/53162615e4b08f2413caa7c2/1433114543363-JZNJMLXI1Q29P6X9TQJ4/ke17ZwdGBToddI8pDm48kM92qaEInPRgHHeE4slqO5tZw-zPPgdn4jUwVcJE1ZvWQUxwkmyExglNqGp0IvTJZamWLI2zvYWH8K3-s_4yszcp2ryTI0HqTOaaUohrI8PIX_nEH5US_0xjPAh8JvCafs-2nCBXRWq9ujg-4y6lu-UKMshLAGzx4R3EDFOm1kBS/hemingway-bar-prague',
        'https://media-cdn.tripadvisor.com/media/photo-s/07/75/74/c3/hemingway.jpg'
    ],
    CategoryEnum.clothing: [
        'https://www.blogto.com/listings/fashion/upload/2014/02/20140126-590-OddFindsGeneralStore-2951.jpg',
        'https://www.prague-stay.com/images/full_image/1920x1200/girls%20without%20clothes%20prague-resize~girls-without-clothes-old-town-boutique.jpeg'
    ],
    CategoryEnum.bakery: [
        'https://i.pinimg.com/originals/c5/26/b8/c526b856b1202e4e870e7b9ee8682201.jpg',
        'https://upload.wikimedia.org/wikipedia/commons/1/15/1.20.10Carlo%27sBakeShopByLuigiNovi1.jpg'
    ],
    CategoryEnum.pets: [
        'https://www.prague-stay.com/images/lifestyle_article/270x200/prague%20just%20your%20friend%203-fit~just-your-friend-pet-store-in-prague.png',
        'https://rumpydog.files.wordpress.com/2013/04/0175.jpg'
    ]
}


# parse place
def parse_place(item, order):
    def cast(number, tp='int'):
        try:
            if tp == 'int':
                return int(number)
            return float(number)
        except:
            return 0

    def select_random_photo(cat_str):
        sel_cat = map_class(item['category'])
        if sel_cat is None:
            return {'https://media-cdn.tripadvisor.com/media/photo-s/12/b1/44/23/caption.jpg'}
        else:
            pictures = list(photos[sel_cat])
            random.shuffle(pictures)
            return set(pictures[:2])

    return Place(
        location_id=str(order),
        location_name=item['title'],
        picture_urls=select_random_photo(item['category']),
        rating=cast(item['totalScore'], tp='float'),
        reviews_cnt=cast(item['reviewsCount']),
        categories={map_class(item['category'])},
        lat=item['location/lat'],
        lon=item['location/lng'],
        address=item['address'],
        web=item['website'],
        phone=item['phone'],
        story=stories[random.randint(0, len(stories) - 1)]
    )


# load all places
items = [parse_place(item, i) for i, item in enumerate(pd.read_csv('places_final.csv').to_dict('records'))]
places: Dict[CategoryEnum, List[Place]] = {
    cat: [] for cat in CategoryEnum
}
places[None] = []
for place in items:
    places.get(list(place.categories)[0]).append(place)

# DB of places
PLACES_BY_ID = {item.location_id: item for item in items}


def make_recommendations() -> List[Recommendation]:
    # make recommendations
    rec = [RecommendationTypeEnum.frequency, RecommendationTypeEnum.frequency, RecommendationTypeEnum.do_again,
           RecommendationTypeEnum.discover]

    # random categories
    categories: List[CategoryEnum] = list(CategoryEnum)
    random.shuffle(categories)
    categories = categories[:len(rec)]

    resluts: List[Recommendation] = []

    # create recommendation for each category - select ID by random
    for index, rec_type in enumerate(rec):
        consider = list(places[categories[index]])
        random.shuffle(consider)

        main_place = consider[0]
        other = consider[1:4]
        recommendation = Recommendation(
            place=main_place,
            user=dummy_profile,
            category=categories[index],
            recommendation_type=rec_type,
            alternatives=set(other)
        )
        resluts.append(recommendation)

    return resluts


make_recommendations()

# dummy data for places
dummy_place = Place(
    location_id='123',
    location_name='Kaava Karlin',
    picture_urls={'https://media-cdn.tripadvisor.com/media/photo-s/12/b1/44/23/caption.jpg'},
    rating=4.9,
    reviews_cnt=31,
    categories={CategoryEnum.coffee, CategoryEnum.eating_out},
    lat=50.0945258,
    lon=14.4535386,
    address='Sokolovská 101, 186 00 Karlín',
    web='https://www.kaava.shop/',
    phone='774 466 968',
    story='Kaava now works in limited mode ′′ windows ", but the e-commerce is still the same. We have a lot of new things for you, which will not only please, but also warm up not only outside, but also at home. A lot of strength and thank you all for your support!'
)
