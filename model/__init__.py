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


class ProfileRankingTypeEnum(enum.Enum):
    """
    Enumeration of ranking types
    """
    supporter = 1
    ambassador = 2
    sponsor = 3
    hero = 4


def get_rank(count_of_alternatives: int) -> ProfileRankingTypeEnum:
    if count_of_alternatives < 15:
        return ProfileRankingTypeEnum.supporter
    elif count_of_alternatives < 30:
        return ProfileRankingTypeEnum.ambassador
    elif count_of_alternatives < 45:
        return ProfileRankingTypeEnum.sponsor
    return ProfileRankingTypeEnum.hero


class AReview(abc.ABC):
    def __init__(self, user_name: str, review: str, rating: float, created: datetime.date):
        self.user_name: str = user_name
        self.review: str = review
        self.rating: float = rating
        self.created: datetime.date = created


class APlace(abc.ABC):
    def __init__(self, location_id: str, location_name: str, picture_urls: Set[str], rating: float, reviews_cnt: int,
                 categories: Set[CategoryEnum], lat: float, lon: float, address: str, web: Optional[str],
                 phone: Optional[str], story: Optional[str]):
        self.location_name: str = location_name
        self.location_id: str = location_id
        self.picture_urls: Set[str] = picture_urls
        self.rating: float = rating
        self.reviews_cnt: int = reviews_cnt
        self.categories: Set[CategoryEnum] = categories
        self.lat: float = lat
        self.lon: float = lon
        self.address: str = address
        self.web: Optional[str] = web
        self.phone: Optional[str] = phone
        self.story: Optional[str] = story

    def __hash__(self):
        return hash(self.location_id)

    def __eq__(self, other):
        return self.__class__ == other.__class__ and self.location_id == other.location_id


class AProfile(abc.ABC):
    def __init__(self, user_id: str, name: str, profile_image_url: Optional[str] = None, alternatives: int = 0):
        self.user_id: str = user_id
        self.name: str = name
        self.alternatives: int = alternatives
        self.profile_image_url: Optional[str] = profile_image_url

    def get_rank(self) -> ProfileRankingTypeEnum:
        return get_rank(self.alternatives)

    def __hash__(self):
        return hash(self.user_id)

    def __eq__(self, other):
        return self.__class__ == other.__class__ and self.user_id == other.location_id


class ARecommendation(abc.ABC):
    def __init__(self, category: CategoryEnum, recommendation_type: RecommendationTypeEnum):
        self.category: CategoryEnum = category
        self.recommendation_type: RecommendationTypeEnum = recommendation_type


class ATransaction(abc.ABC):
    def __init__(self, created: datetime.date):
        self.created: datetime.date = created
