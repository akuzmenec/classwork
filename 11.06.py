# #1
# a = int(input())
# b = int(input())
# s = 0
# if a > b:
#     a,b = b,a
# while a > b:
#     s += a
#     a += 1

# #2
#
# a = int(input())
# b = int(input())
# if a > b:
#     a, b = b, a
# while a < b:
#     b -= 1
#     print(b)
#
# #3
# minimum = 0
# while True:
#
#     a = int(input())
#     if a == 0:
#         break
#
#     if minimum > a or minimum == 0:
#         minimum = a
#
#     print(minimum)

# min_1 = int(input())
# max_1 = int(input())
# min_2 = int(input())
# max_2 = int(input())
# if min_1 > max_2: min_1, max_1 = max_1, min_1
# if min_2 > max_2: min_2, max_2 = max_2, min_1
### в тел
# if min_1 > min_2:
#     min = min_1
# else:
#     min = min_2
#
# if max_1 < max_2:
#     max = max_1
# else:
#     max = max_2
#
# while min <= max:
#     print(min)
#     min += 1
#
# a = int(input())
#
# print(a % 2 and "четное" or "нечетное")


########### FOR

n = int(input())
# if  % 2 == 0:
for i in range(n):
    num = int(input())
    if num%2 == 0:
        print(num, end=" ")
# else:
#     a += 1
#     for i in range(a, b+1, 2):
#         print(i, end=" ")
# #
# a = int(input())
# b = int(input())
# s = 0
# k = 0
#
# if a > b:
#     a, b = b, a
# for i in range(a, b+1, 1):
#     s += i
#     k += 1
# print(s/k)

# s = (a+b)/2
# print(s)
# if a > b:
#     a, b = b, a
# a = 1
#
# for i in range(a, b+1, 1):
#     a *= i
# print(a)

# n = int(input())
# for i in range(n):
#     a = int(input())
#     if a > m:
#         m = a
# print(m)


