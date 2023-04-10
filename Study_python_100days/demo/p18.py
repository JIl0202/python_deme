# import random
#
# # 产生一个1~99之间的随机数
# x = random.randint(1, 9)
#
# print("============幸运大抽奖开始===============")
#
# while True:
#     number1 = int(input("请输入一个数字，1~9之间："))
#     num_list = [0,1,2,3,4,5,6,7,8,9]
#     if number1 != num_list[number1]:
#         print('输入错误,请重新输入')
#         continue
#     elif number1 == x:
#         print("这么难都能中，了不起，恭喜中了大奖！")
#         break
#     else:
#         if number1 > x:
#             print("很遗憾没猜中，数字大了")
#         else:
#             print("很遗憾没猜中，数字小了")
#         flag = input("需要帮助吗？输入y或者n：")
#         if flag == "y":
#             print("答案是", x)
#         else:
#             e1 = input("要退出吗？输入y或者n：")
#             if e1 == "y":
#                 print("游戏结束")
#                 break
#             else:
#                 print("游戏继续")
#                 continue
#                 print("执行continue，后面的语句被忽略")
#
#
# print("====================游戏结束============================")

# 列表的遍历
# nlist = [4, 5, 6, 7, 8, 9, 12, 20, 36]

# i = 0
# while i < len(nlist):
#     print(nlist[i])
#     i += 1

# for 临时变量 in 列表或者元组
# for n in nlist:
#     print("n is: ", n)
# #
# #
# str1 = "abcdefg"
# for x in str1:
#     print(x)
#
# import time
# print("===============午饭时间到，开始吃包子==============")
# n1 = int(input("今天吃汤包，请问吃几笼："))
# for i in range(n1):
#     print("开始吃第%d笼" % (i+1))
#     for j in range(6):
#         print("现在是第%d笼的第%d个包子" % (i+1, j+1))
#         time.sleep(1)
#
#     if i < n1:
#         print("第%d笼吃完了，开始下一个" % (i+1))
#
# print("吃饱了，吃撑了")
#
#
# list1 = [0,1,2,3,4,5,6,7,8,9]
# list2 = [10, 11,12,13,14,15,16,17,18,19]
# str1 = "hello world"
# for x in range(3000):
#     print(x)
#
# # 参数默认值，当调用时没有传值给参数，形参按默认值处理
# # 当参数有的有默认值，有的没有，没有默认值的参数，要写在有默认值的参数前面
# def greeting(number=2, name="诸葛亮"):
#     for i in range(number):
#         print("你好，", name)
#
#
# # 函数的调用
# greeting(3, "曹操")
# greeting(5, "刘备")
# greeting()
#
# # 自动售烟机模拟器
# def sale(type, money):
#     if type==1 and money==10:
#         return "红双喜"
#     if type==2 and money==30:
#         return "黄鹤楼"
#     if type==3 and money==100:
#         return "1916"
#     else:
#         return "钱或者选择错误，购买失败"
#
#
#
# t1 = int(input("请选择商品编号："))
# m1 = int(input("请扫码支付："))
# goods = sale(t1, m1)
# print("购买完成，结果是：%s" % goods)


# import time as t
#
#
# t1 = t.time()  # 打印时间戳，也称为UNIX时间，自1970年1月1日0点0分0秒到目前为止，累积的毫秒数
# print(t1)
# for i in range(100000):
#     t.sleep(2)
#     print("循环中第%d次" % i)
# #
# t2 = t.time()
# print("循环 %d 次用了多少 %.4f 秒：" % (i, t2 - t1))
#
# while True:
#     print('当前时间是:', t.strftime("%Y-%m-%d %H:%M:%S", t.localtime()))
#     t.sleep(1)

print("%-13s%-13s%-13s" % ("name", "age", "height"))  # 打印表格
print("%-13s%-13d%-13.2f" % ("James", 19, 1.7856))
print("%-13s%-13d%-13.2f" % ("xxx", 33, 18))
