"""
from collections.abc import *

message = " any way "

print(f"{message.lstrip()}")  # 去掉字符串左边空格
print(f"{message.rstrip()}")  # 去掉字符串左边空格
print(f"{message.strip()}")  # 去掉字符串两边空格
print(f"{message.title()}")  # 字符串首字母大写
print(f"{message.upper()}")  # 所有字符串大写
print(f"{message.lower()}")  # 所有字符串小写

print(dir(object))

import abc


class Animals(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def say(self):
        print("is a Animal")

    def a(self):
        print("Animal's a")
        raise NotImplementedError


class Cat(Animals):

    def say(self):
        print("I am a Cat")

    def a(self):
        print("Cat's a ")

    def b(self):
        print("b")


animal = Cat()
animal.a()
print(type(animal))
"""

date_str = "2023-12-26"
year, month, day = tuple(date_str.split("-"))


