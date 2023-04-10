# # 以下函数，不会改变列表自身
# numlist = [7, 8, 9, 10, 1, 2, 3, 4, 5]
# # 不改变列表
# print("""
# 列表长度是：{}
# 列表的最后一个值是：{}
# 最大值是：{}
# 最小值是：{}
# 列表顺序排列为\n{}
# 列表逆序排列为\n{}
# 列表元素为\n{}
# """.format(
# len(numlist),
# numlist[len(numlist) - 1],
# max(numlist),
# min(numlist),
# sorted(numlist),
# sorted(numlist,reverse=False),
# numlist))
#
#
# # 以下函数都会改变列表自身
# numlist = [7, 8, 9, 10, 1, 2, 3, 4, 5]
# # 在列表末尾追加新值
# numlist.append(33)
# print('末尾添加1\n',numlist)
#
# numlist.insert(len(numlist),34)
# print('末尾添加2\n',numlist)
# # 在指定索引位置添加新值
# numlist.insert(0, 520)
# print('脚标0位添加\n',numlist)
# numlist.insert(4, 88)
# print('脚标4位添加\n',numlist)
# #反转列表
# numlist.reverse()
# print("反转排列\n",numlist )
# #逆序排列
# numlist.sort(reverse=True)
# print("逆序排列\n", numlist)
# #顺序排列
# numlist.sort()
# print("顺序排列\n ", numlist)
