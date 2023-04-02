import random
#
def main():
    tmp = input("输入任意值开始游戏")
    while tmp != 'q':
        b = input("请输入石头,剪刀,布")
        if b == "石头":
            c = 0
        elif b == "剪刀":
            c = 1
        elif b == "布":
            c = 2
        else:
            print("您的输入不符合规范,游戏结束")
            break
        a = random.randint(0, 2)
        if c - a == 1:
            print("computer win")
        elif c - a == 2:
            print("you win")
        elif c - a == -2:
            print("computer win")
        elif c - a == -1:
            print("you win")
        elif c - a == 0:
            print("play again")
        tmp = input("是否再来一局? 如果输入q则退出.")

main()

#石头=0
#剪刀=1
#布=2

# option = ['石头','剪刀','布']
#
# pwin = 0	# 玩家获胜次数
# cwin = 0	# 电脑获胜次数
#
# win_list = [['石头','剪刀'],['剪刀','布'],['布','石头']]
#
# while pwin < 2 and cwin < 2 :	# 三局两胜制
# 	cpu = random.choice(option)	# 电脑的三种可能结果
# 	i = int(input("请选择：\n[0]石头[1]剪刀[2]布\n"))	# 给出三个选项，方便用户
# 	player = option[i]	#	玩家的结果
# 	print("你出： %s , 电脑出： %s" % (player,cpu))
# 	if player == cpu :
# 		print("\033[32;1m平局\033[0m")
# 		print("目前比分： 玩家 %s : 电脑 %s " % (pwin,cwin))
# 	elif [player,cpu] in win_list :
# 		print("\033[31;1m你赢了\033[0m")
# 		pwin += 1
# 		print("目前比分： 玩家 %s : 电脑 %s " % (pwin,cwin))
# 	else :
# 		print("\033[33;1m你输了\033[0m")
# 		cwin += 1
# 		print("目前比分： 玩家 %s : 电脑 %s " % (pwin,cwin))
# if pwin > cwin :
# 	print("游戏结束！最终比分： 玩家 %s : 电脑 %s ，\033[31;1m玩家获胜！\033[0m" % (pwin,cwin))
# else :
# 	print("游戏结束！最终比分： 玩家 %s : 电脑 %s ，\033[32;1m电脑获胜！\033[0m" % (pwin,cwin))
