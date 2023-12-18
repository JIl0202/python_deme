value = 'todyisvaryhappy'
list_1 = value.split('a')
list_2 = tuple(list_1)
print("""
列表1内容
{}
列表1内容
{}
列表1类型为
{}
列表2类型为
{}
"""
      .format(list_1, list_2, type(list_1), type(list_2)))

# 列表和元组的切片，切片的第三个参数，是步进值，就是每间隔多少个数取一次值，切片不包含后一个索引的值
numlist = (7, 8, 9, 10, 1, 2, 3, 4, 5)
# print(numlist[-1])
print(numlist[3:8])
print(numlist[:6])
print(numlist[:])
print(numlist[2:])
print(numlist[3:-2])
print(numlist[::1])
print(numlist[::-1])
print(numlist)
#
str1 = "博为峰武汉校区109班"
print(len(str1))
slist = str1[3:5]
print(slist)
print(type(slist))

# 元组定义tuple
t1 = ("a", "b", "c", "d")
# 查看元组类型
print("t1的类型是：", type(t1))
# 通过下标操作元组
print(t1[2])
# 查看元组的长度
print("长度是：", len(t1))

#
food = ("烧牛肉", "土豆丝", "辣椒炒肉")
print("food 类型是：", type(food))
print(food[1])
# #
#
foodlist = list(food)
#
print("foodlist的类型是：", type(foodlist))
foodlist.append("热干面")
print(foodlist)
# #
nlist = ["卧龙", "凤雏", "冢虎"]
tn = tuple(nlist)
print("tn的类型是：", type(tn))

str1 = "a,b,c,d,e"
# ["a", "b", "c", "d", "e"]
slist = str1.split(",")
#
print("slist len is ", len(slist))
print(slist[3])
print(type(slist))
print(slist)
# #
str2 = "123:2:45:900:456"
slist2 = str2.split(":")
print(slist2)
# #
str3 = "eabacadaf"
slist3 = str3.split("a")
print(slist3)

strlist = input("请输入一组数字，使用, 分隔开：").split(",")

# strlist = input("请输入一组数字，使用, 分隔开：").split(",")
# #
print("长度是：", len(strlist))
print("内容是：", strlist)
