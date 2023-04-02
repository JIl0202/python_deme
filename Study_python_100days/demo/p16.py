"""
# 列表中的元素是字典
s1 = {"name": "关羽", "age":50}
s2 = {"name": "张飞", "age":48}
s3 = {"name": "赵云", "age":46}

hero = [s1, s2, s3]

print(hero[1]["name"])
print(hero[0].get("name"))
# #
# # 字典中包含有列表
f1 = {"name":"大米先生", "food":["烧牛肉", "土豆丝", "辣椒炒肉"]}
f2 = {"name":"沙县小吃", "food":["黄焖鸡", "飘香面", "卤鸡腿"]}

print(f1.get("food")[0])
print(f2.get("name"), f2.get("food")[1])
#
# # 字典中包含有字典
f3 = {"name":"沙县小吃", "food":{"进店必点":"黄焖鸡", "招牌面点":"飘香面", "五一特价":"卤鸡腿"}}
print(f3["food"]["五一特价"])
print(f3.get("food").get("招牌面点"))
"""