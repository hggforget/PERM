import typing


class Matcher:
    def __init__(self, condition):
        self.condition = condition

    def __repr__(self):
        return "<Matcher({})>".format(self.to_dict())

    def __str__(self):
        return self.condition

    def to_dict(self, ):
        return {k: v for k, v in self.__dict__.items()}

    @classmethod
    def from_dict(cls, recorde: typing.Dict):
        return Matcher(
            condition=recorde.get('condition', '')
        )