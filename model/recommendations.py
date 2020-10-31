"""Recommendation Entities"""
from typing import Set

from model import CategoryEnum, RecommendationTypeEnum, ARecommendation, APlace, AProfile


class Recommendation(ARecommendation):

    def __init__(self, place: APlace, user: AProfile, category: CategoryEnum,
                 recommendation_type: RecommendationTypeEnum, alternatives: Set[APlace]):
        super().__init__(category, recommendation_type)
        self.place: APlace = place
        self.user: AProfile = user
        self.alternatives: Set[APlace] = alternatives

    def __hash__(self):
        return hash((self.place, self.user, self.recommendation_type, self.category))

    def __eq__(self, other):
        return self.__class__ == other.__class__ and self.place == other.place and self.user == other.user \
               and self.recommendation_type == other.recommendation_type and self.category == other.category
