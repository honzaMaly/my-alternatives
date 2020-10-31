"""Profile Entities"""
from typing import Set, Optional

from model import AProfile, ATransaction, ARecommendation


class Profile(AProfile):
    def __init__(self, user_id: str, name: str, profile_image_url: Optional[str] = None, alternatives: int = 0):
        super().__init__(user_id, name, profile_image_url, alternatives)
        self.transactions: Set[ATransaction] = set()
        self.recommendations: Set[ARecommendation] = set()

    def add_recommendation(self, review: ARecommendation):
        self.recommendations.add(review)

    def add_transaction(self, transaction: ATransaction):
        self.transactions.add(transaction)
