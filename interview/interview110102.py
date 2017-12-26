# -*- coding: utf-8 -*-


_G = {"counter": 99, "user": "admin"}


class Refs():
    def __init__(self, name=None):
        self.name = name
        self._G = _G
        self.init = self._G['counter']

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self._G["counter"] = self.init
        return False

    def acc(self, n=1):
        self._G["counter"] += n

    def dec(self, n=1):
        self._G["counter"] -= n

    def __str__(self):
        return "COUNTER #{name}: {counter}".format(name=self.name, **self._G)


with Refs("ref1") as ref1, Refs("ref2") as ref2:  # Python 3.1 加入了多个并列上下文管理器
    for _ in range(3):
        ref1.dec()
        print(ref1)
        ref2.acc()
        print(ref2)
print(_G)