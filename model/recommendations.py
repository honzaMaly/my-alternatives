"""Recommendation Entities"""
from model import CategoryEnum, RecommendationTypeEnum, ARecommendation, APlace, AProfile


class Recommendation(ARecommendation):

    def __init__(self, place: APlace, user: AProfile, category: CategoryEnum,
                 recommendation_type: RecommendationTypeEnum):
        super().__init__(category, recommendation_type)
        self.place: APlace = place
        self.user: AProfile = user
