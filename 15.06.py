# #1
#
# s = 0
# a = int(input())
# b = int(input())
# if a>b:a,b=b,a
# for i in range(a,b+1):
#     s += i
# print(s)
#
# #2
# n = int(input())
# if n>=0:
#     for i in range(0, n-1, -1):
#         print(i, end=" ")
# else:
#     for i in range(n, -1, -1):
#         print(i, end=" ")
#
# #3
# n = int(input())
# f = 1
# for i in range(1, 5+1):
#
#     f *= i
# print(f)
# #
# #4
# a = int(input())
# max = a
# for i in range(3):
#     a = int(input())
#     if max < a:
#         max = a
# print(max)
# #5
# s = 0
# for i in range(5):
#     a = int(input())
#     if a//100 > 0 and a//1000 == 0:
#         s += a
#
# print(s)
# column = int(input())
# row = int(input())
# k = 1
# for i in range(1, row+1):
#     for g in range(1, column+1):
#         print(f"{i}:{g}", end=" ")
#     print()

# a = int(input())
# for i in range(a):
#     print(" " * (a-i) + "* "* i + " "*(a-i))
#
# a = int(input())
# for i in range(a, 0, -1):
#     print(" " * (a-i) + "* " * i + " "*(a-i))
#
# a = int(input())
# for i in range(0, a):
#     print("* " * a)
#     if i == 0 or i == a-1:
#         print("* " * a)
#     else:
#         print("*" , " " * (a-1), "*" )
#

# a = int(input())
#
# print("* " * a)
#
# for i in range(a-2):
#     print("* " + "  " * (a-2) + "*")
# print("* " * a)
#
# a = int(input())
# for i in range((a+1)//2):
#     print("  "* i + "* "*(a-i*2))
