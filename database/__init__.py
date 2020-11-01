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


# TODO: photos - per category - 10
# TODO: stories

# parse place
def parse_place(item, order):
    def cast(number, tp='int'):
        try:
            if tp == 'int':
                return int(number)
            return float(number)
        except:
            return 0

    return Place(
        location_id=str(order),
        location_name=item['title'],
        picture_urls={'https://media-cdn.tripadvisor.com/media/photo-s/12/b1/44/23/caption.jpg'},
        rating=cast(item['totalScore'], tp='float'),
        reviews_cnt=cast(item['reviewsCount']),
        categories={map_class(item['category'])},
        lat=item['location/lat'],
        lon=item['location/lng'],
        address=item['address'],
        web=item['website'],
        phone=item['phone'],
        story='Kaava now works in limited mode ′′ windows ", but the e-commerce is still the same. We have a lot of new things for you, which will not only please, but also warm up not only outside, but also at home. A lot of strength and thank you all for your support!'
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
