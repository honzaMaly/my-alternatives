"""Transaction Entities"""
import datetime

from model import ATransaction, AProfile, APlace


class Transaction(ATransaction):
    def __init__(self, created: datetime.date, user: AProfile, place: APlace):
        super().__init__(created)
        self.user: AProfile = user
        self.place: APlace = place

    def __hash__(self):
        return hash((self.place, self.user, self.created))

    def __eq__(self, other):
        return self.__class__ == other.__class__ and self.place == other.place and self.user == other.user \
               and self.created == other.created
