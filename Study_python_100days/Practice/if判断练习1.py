def Judgment_age():
    age = int(input("请输入年龄："))

    if age >= 30:
        print("成熟稳重")
        print("花有重开日")
        print("人无再少年")
    else:
        print("青春年少")
        print("少壮不努力，老大徒伤悲")

    print("程序结束")


def Judgment_wage():
    sal = int(input("请问月收入多少："))

    if sal >= 3000:
        print("工资大于等于3000，等级是A")
        print("为真的时候，才执行这条语句，缩进表示这条语句受到if的控制")
    elif sal >= 1500:
        print("工资在3000到1500之间，等级是B")
        print("为假的时候，才执行这条语句，缩进表示这条语句收到if的控制")
    elif sal >= 1000:
        print("工资在1500到1000之间，等级是C")
    else:
        print("工资低于1000，等级是D")

    print("判断完成")


def bool_0():
    x = 10 - 10
    n1 = 0
    age = 26
    ename = "诸葛亮"
    flag = None
    b = ''
    list_1 = [x, n1, age, ename, flag, b]
    for enum in list_1:
        if enum:
            print(f"{enum} 条件为真")
        else:
            print(f"{enum} 条件为假")


if __name__ == '__main__':
    bool_0()
