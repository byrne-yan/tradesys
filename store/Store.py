import abc


class Store(abc.ABC):
    '持久化抽象接口'


def get_candidates(self):
    raise NotImplementedError


def get_holds(self):
    raise NotImplementedError


def get_stock(self):
    raise NotImplementedError
