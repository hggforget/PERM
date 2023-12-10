import typing


class Request:
    def __init__(self, sub, obj, act=None):
        self.sub = sub
        self.obj = obj
        self.act = act

    def __repr__(self):
        return "<Request({})>".format(self.to_dict())

    def __str__(self):
        return '{}, {}, {}'.format(self.sub, self.obj, self.act)

    def to_dict(self, ):
        return {k: v for k, v in self.__dict__.items()}

    @classmethod
    def from_dict(cls, recorde: typing.Dict):
        return Request(
            sub=recorde.get('sub', ''),
            obj=recorde.get('obj', ''),
            act=recorde.get('act', ''),
        )
