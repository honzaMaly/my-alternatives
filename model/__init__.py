import abc
import datetime
import enum
from typing import Set, Optional


class CategoryEnum(enum.Enum):
    """
    Enumeration of categories
    """
    coffee = 1
    eating_out = 2


class RecommendationTypeEnum(enum.Enum):
    """
    Enumeration of recommendation types
    """
    frequency = 1
    do_again = 2
    discover = 3


class AReview(abc.ABC):
    def __init__(self, user_name: str, review: str, rating: float, created: datetime.date):
        self.user_name: str = user_name
        self.review: str = review
        self.rating: float = rating
        self.created: datetime.date = created


class APlace(abc.ABC):
    def __init__(self, location_id: str, location_name: str, picture_urls: Set[str], rating: float, reviews: int,
                 categories: Set[CategoryEnum], lat: float, lon: float, address: str, web: Optional[str],
                 phone: Optional[str], story: str):
        self.location_name: str = location_name
        self.location_id: str = location_id
        self.picture_urls: Set[str] = picture_urls
        self.rating: float = rating
        self.reviews: int = reviews
        self.categories: Set[CategoryEnum] = categories
        self.lat: float = lat
        self.lon: float = lon
        self.address: str = address
        self.web: Optional[str] = web
        self.phone: Optional[str] = phone
        self.story: str = story


class AProfile(abc.ABC):
    def __init__(self, user_id: str):
        self.user_id: str = user_id


class ARecommendation(abc.ABC):
    def __init__(self, category: CategoryEnum, recommendation_type: RecommendationTypeEnum):
        self.category: CategoryEnum = category
        self.recommendation_type: RecommendationTypeEnum = recommendation_type


class ATransaction(abc.ABC):
    def __init__(self, transaction_id: str, created: datetime.date):
        self.created: datetime.date = created
        self.transaction_id: str = transaction_id
