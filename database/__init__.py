import datetime

from model import CategoryEnum, RecommendationTypeEnum
from model.places import Place, Review
from model.profiles import Profile
from model.recommendations import Recommendation

# dummy profile
dummy_profile = Profile(
    '10', 'John Doe', 'https://i.pinimg.com/originals/c8/f7/a8/c8f7a86a5a668cac7a2846073ce4baf3.jpg', 20)

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

# dummy data for ratings
dummy_place_rating_0 = Review(
    user_name='Kateřina Eklová',
    review='Delicious coffee, original "lilac" lemonade, nice staff, small but cosy interior, nice outdoor seating area - everything transformer this formerly ugly corner of the street.',
    rating=5.0,
    created=datetime.date(2020, 10, 28)
)
dummy_place.add_review(dummy_place_rating_0)
dummy_place_rating_1 = Review(
    user_name='Guido Deutsch',
    review='Excellent coffee, professional prepared - you can decide how much hot water should be added to your Americano, for instance. If you search EXCELLENT coffee this is my first suggestion.',
    rating=4.0,
    created=datetime.date(2019, 10, 28)
)
dummy_place.add_review(dummy_place_rating_1)

# dummy recommendation
dummy_recommendation = Recommendation(
    place=dummy_place,
    user=dummy_profile,
    category=CategoryEnum.coffee,
    recommendation_type=RecommendationTypeEnum.frequency,
    alternatives={dummy_place, dummy_place}
)
