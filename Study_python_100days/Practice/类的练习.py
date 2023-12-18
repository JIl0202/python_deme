class person:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def act(self, adder):
        self.adder = adder
        return self.name + self.sex + self.age + "现在家住" + self.adder


class ikun(person):
    def __init__(self, name, age, sex, birth):
        super(ikun, self).__init__(name, age, sex)
        self.birth = birth

    def sal(self):
        return self.name + '出生于' + self.birth + '工资不详'


if __name__ == '__main__':
    p1 = person("张三", "25岁", "男")
    p2 = person("菜虚鲲", "20岁", "男")
    print(p2.act('北京'))
    p3 = ikun('菜菜', '20', '女', '河南')
    print(p3.__dict__)
    print('\n', p1, '\n', p2, '\n', p3)

for i in range(3):
    list.append()
