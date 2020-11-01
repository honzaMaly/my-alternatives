from model import CategoryEnum, RecommendationTypeEnum
from model.places import Place
from model.profiles import Profile
from model.recommendations import Recommendation

# dummy profile
dummy_profile = Profile(
    '10', 'John Doe', 'https://i.pinimg.com/originals/c8/f7/a8/c8f7a86a5a668cac7a2846073ce4baf3.jpg', 20)

# mapping categories



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

# dummy recommendation
dummy_recommendation = Recommendation(
    place=dummy_place,
    user=dummy_profile,
    category=CategoryEnum.coffee,
    recommendation_type=RecommendationTypeEnum.frequency,
    alternatives={dummy_place, dummy_place}
)
