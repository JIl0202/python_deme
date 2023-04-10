from p1 import *
import time as t

t1 = t.time()
m = int(input('请输入项数'))
i = 1
while i <= m:
    print(fibonacci_1(i), end='\t')
    i += 1
print('')

fibonacci_2(m)

t2 = t.time()
x = t2 - t1
print('\n总共耗时%.2f' % x)
