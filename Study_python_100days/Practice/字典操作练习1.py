
s1 = {"empno": 9527, "ename": "华安", "job": "书童", "sal": 8888.88, "deptno": 10}

# mysql = {"empno": 9527, "eanme":"华安", "job":"书童"}
# 字典是一种KV结构，K是key，中文键，V是value，也就是值，一对KV称为一个键值对
# 字典包含有若干个键值对，但是，在一个字典中，key，键是唯一的，不可重复，值可以重复
print("s1的类型是：", type(s1))
print("字典的内容是：", s1)
print(len(s1))

print(s1["job"])
print(s1.get("书童"))
# # s1[key]，字典是通过key，键查找对应的值，但是不能通过值反向查找键
print(s1["job"], s1["sal"])
print("字典的值列表是：", s1.values())
print("字典的键列表是：", s1.keys())
print("字典的键值对的列表是：", s1.items())
s1.pop("ename")
print("字典的内容是：", s1)

s1["kk"] = "luna"
print(s1)

