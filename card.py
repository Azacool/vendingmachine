class Card:
    def __init__(self, id, credit) -> None:
        self._id = id
        self._credit = credit

    def add_sum(self, value):
        self._credit += value

    @property
    def cretid(self):
        return self._credit

    