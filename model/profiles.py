"""Profile Entities"""
from typing import Set

from model import AProfile, ATransaction, ARecommendation


class Profile(AProfile):
    def __init__(self, user_id: str):
        super().__init__(user_id)
        self.transactions: Set[ATransaction] = set()
        self.recommendations: Set[ARecommendation] = set()

    def add_recommendation(self, review: ARecommendation):
        self.recommendations.add(review)

    def add_transaction(self, transaction: ATransaction):
        self.transactions.add(transaction)
