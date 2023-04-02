# def numlist(n):
#
#     print(n)
#     if n == 1:
#         return 1
#     return numlist(n-1)
#
# numlist(100)
# def fib(n):
#     if n ==0 or n == 1:
#         return 1
#     res = 0
#     fib0 = 0
#     fib1 = 1
#     for i in range(2,n):
#         print(f'res={res},fib0={fib0},fib1={fib1}')
#         res = fib0 + fib1
#         fib0 = fib1
#         fib1 = res
#     return res
#
# fib(5)

# m,n = '2345','tianxiadayitong'
# if n.isdigit() or m.isdigit():
#     print(5)
# else:
#     print('其中没有数字')

# num1=[10,[2,3,5]]
# num2=num1[:]
# num1[1].append(5)
#
# print(num1,id(num1))
# print(num2,id(num2))

a = 'tianxiadayitong'
b = {1,2,5,5,6,7,2,1}
print(a[4:11])
print(b, type(b))
