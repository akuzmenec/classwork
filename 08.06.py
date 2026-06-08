# #1
# a = int(input())
# b = int(input())
# c = int(input())
#
# if (a > c) and (a > b):
#     print(a)
# elif (b > a) and (b > c):
#     print(b)
# elif (c > a) and (c > b):
#     print(c)
#
# #2
# d = int(input())
# if d % 2 == 0:
#     print("yes")
# else:
#     print("no")
#
# #3
# e = int(input())
#
# if (e//10 == 3) or (e % 10 == 3):
#     print("yes")
# else:
#     print("no")
#
# #4
# f = int(input())
#
# if (f > 10) and (f < 20):
#     print("yes")
# else:
#     print("no")
# #5
#
# g = int(input())
# h = int(input())
#
# if (g % 3 == 0) and (h % 3 == 0):
#     print("yes")
# else:
#     print("no")


########## cycle


# a = int(input())
# b = int(input())
# p = 0
# while p <= a:
#     print(p, end=" ")
#     p += 1
#
# if a > b:
#     a, b = b, a
# while a <= b:
#     print(b, end=" ")
#     b -= 1
#
#all even number
# while b <= a:
#     print(b, end=" ")
#     b += 2
# or
#
# while b <= a:
#     if b % 2 == 0:
#         print(b, end=" ")
#     b += 1
# if a > b: a, b = b, a
# if a % 2: a += 1
# while a <= b:
#     print(a, end=" ")
#     a += 2
k = 0
s = 0
n = int(input())
while k < n:
    num = int(input())
    s += num
    k += 1
print(s)

