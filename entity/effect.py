import typing


class Effect:
    def __init__(self, policy_effect):
        self.policy_effect = policy_effect

    def __repr__(self):
        return "<Effect({})>".format(self.to_dict())

    def __str__(self):
        return self.policy_effect

    def to_dict(self, ):
        return {k: v for k, v in self.__dict__.items()}

    @classmethod
    def from_dict(cls, recorde: typing.Dict):
        return Effect(
            policy_effect=recorde.get('policy_effect', '')
        )
