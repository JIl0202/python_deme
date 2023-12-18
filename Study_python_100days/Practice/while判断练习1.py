
import time

i = 0
while True:
    print("这是一个死循环，正常情况下不会结束")
    time.sleep(2)
    i += 1
    if i >= 10:
        print("i的值是 %d" % i)
        print("条件为真，调用break，结束循环")
        # break只能出现在循环内部（循环体），作用是立即结束循环
        break

print("由于我们调用了break，死循环也结束了")

i = 0
while i <= 10:
    i += 1
    if i % 2 != 0:
        # print("是奇数，跳过打印")
        # continue和break一样，用在循环体内部，作用是跳过循环体其后的语句，重新开始循环
        continue
    print(i)

print("程序结束")

