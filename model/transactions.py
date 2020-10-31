"""Transaction Entities"""
import datetime

from model import ATransaction, AProfile, APlace


class Transaction(ATransaction):
    def __init__(self, transaction_id: str, created: datetime.date, user: AProfile, place: APlace):
        super().__init__(transaction_id, created)
        self.user: AProfile = user
        self.place: APlace = place
