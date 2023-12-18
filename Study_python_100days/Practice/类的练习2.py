class Father(object):
    name = "王大锤"
    height = None

    def __init__(self, money):
        self.____money = money

    @classmethod
    def grep_year(cls):
        cls.year = 55
        print('name', cls.name, 'age', cls.year)

    @staticmethod
    def grep2():
        Father.height = str(176) + "cm"

    @property
    def set_money(self):
        return self.____money

    @set_money.setter
    def set_money(self, money):
        self.____money = money

    def grep(self):
        return print("当前金钱剩余:\n", self.____money)


class Son(Father):
    def __init__(self, money, age):
        super(Son, self).__init__(money)  # super().__init__(money) 可以获得与前面同样的效果
        self._age = age

    @property
    def year(self):
        return self._age

    @year.setter
    def year(self, age):
        self._age = age

    def son_grep(self):
        print(self._age)


if __name__ == '__main__':
    p2 = Son(money=2000, age=20)
    p2.grep()
    print(p2._age)
    p2.set_money = 20000
    p2.grep()
    p2.grep2()
    print(Father.height)
