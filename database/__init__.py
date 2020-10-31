import datetime

from model import CategoryEnum
from model.places import Place, Review

# dummy data for places
kaava_karlin = Place(
    location_id='123',
    location_name='Kaava Karlin',
    picture_urls=set('https://media-cdn.tripadvisor.com/media/photo-s/12/b1/44/23/caption.jpg'),
    rating=4.9,
    reviews=31,
    categories={CategoryEnum.coffee, CategoryEnum.eating_out},
    lat=50.0945258,
    lon=14.4535386,
    address='Sokolovská 101, 186 00 Karlín',
    web='https://www.kaava.shop/',
    phone='774 466 968',
    story='Kaava now works in limited mode ′′ windows ", but the e-commerce is still the same. We have a lot of new things for you, which will not only please, but also warm up not only outside, but also at home. A lot of strength and thank you all for your support!'
)

# dummy data for ratings
kaava_karlin_rating_0 = Review(
    user_name='Kateřina Eklová',
    review='Delicious coffee, original "lilac" lemonade, nice staff, small but cosy interior, nice outdoor seating area - everything transformer this formerly ugly corner of the street.',
    rating=5.0,
    created=datetime.date(2020, 10, 28)
)
kaava_karlin.add_review(kaava_karlin_rating_0)
kaava_karlin_rating_1 = Review(
    user_name='Guido Deutsch',
    review='Excellent coffee, professional prepared - you can decide how much hot water should be added to your Americano, for instance. If you search EXCELLENT coffee this is my first suggestion.',
    rating=4.0,
    created=datetime.date(2019, 10, 28)
)
kaava_karlin.add_review(kaava_karlin_rating_1)