class Person(object):

    def __init__(self, name, year):
        self._name = name
        self._year = year

    # 访问器 - getter方法
    @property
    def name(self):
        return self._name

    # 访问器 - getter方法
    @property
    def age(self):
        return self._year

    # 修改器 - setter方法
    @age.setter
    def nian(self, year):
        self._year = year

    def play(self):
        if self._year <= 16:
            print('%s正在玩飞行棋.' % self._name)
        else:
            print('%s正在玩斗地主.' % self._name)


def main():
    person = Person('王大锤', 12)
    person.play()
    person.nian = 22
    person.play()
    person.money = 15
    print(person.money)
    # person.name = '白元芳'  # AttributeError: can't set attribute


if __name__ == '__main__':
    print('hello world!')
    main()
