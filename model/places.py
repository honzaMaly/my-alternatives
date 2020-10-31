"""Places Entities"""
import datetime
from typing import Set, Optional, List

from model import CategoryEnum, APlace, AReview, ATransaction


class Place(APlace):
    def __init__(self, location_id: str, location_name: str, picture_urls: Set[str], rating: float, reviews_cnt: int,
                 categories: Set[CategoryEnum], lat: float, lon: float, address: str, web: Optional[str],
                 phone: Optional[str], story: Optional[str]):
        super().__init__(location_id, location_name, picture_urls, rating, reviews_cnt, categories, lat, lon, address,
                         web, phone, story)
        self.reviews: List[AReview] = list()
        self.transactions: Set[ATransaction] = set()

    def add_review(self, review: AReview):
        self.reviews.append(review)

    def add_transaction(self, transaction: ATransaction):
        self.transactions.add(transaction)


class Review(AReview):
    def __init__(self, user_name: str, review: str, rating: float, created: datetime.date):
        super().__init__(user_name, review, rating, created)
