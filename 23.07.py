from random import randint

# #1
# a = int(input())
# max = a
# for i in range(4):
#     a = int(input())
#     if a > max:
#         max = a
# print(max)

# #2
# a = int(input())
# b = int(input())
# if a > b:
#     a,b = b,a
# for i in range(b, a+1, -1):
#     print(i)

# #3
#
# size = int(input())
# k = 5
# sc = []
# for i in range(size):
#     row = []
#     for j in range(size):
#         row.append(k)
#         k += 1
#     sc.append(row)
# for row in sc:
#     print(row)




# #4
#
# a = input()
# if a.isupper() and a.isalpha():
#     print("yes")
# else:
#     print("no")

# #5
# ls = []
# for i in range(0, 24, 3):
#     ls.append(i)
# print(ls)

# #6,7
# a = int(input())
# b = int(input())
# if a>b:
#     a,b = b,a
# ls = [[], []]
# for i in range(5):
#     ls[0].append(randint(a, b+1))
#     ls[1].append(randint(a, b+1))
# print(ls)
# avg = sum(ls[0]) + sum(ls[1]) / 10
# print(avg)
#
# min = 0
# max = 0
#
# for i in range(len(ls)):
#     for j in range(len(ls[i])):
#         if ls[i][j] > max:
#             max = ls[i][j]
#         if ls[i][j] < min:
#             min = ls[i][j]




# #8
#
# ls = [1, 2, 3, 4, 5]
# a = int(input())
# def in_ls(a, ls):
#     flag = "no"
#     for i in ls:
#         if a == i:
#             flag = "yes"
#             break
#     return flag
#
#
# print(in_ls(a, ls))

# #9
# ls = [1, 2, 3, 4, 5]
# def type_num(ls):
#     num = []
#     for i in ls:
#         if i%2 == 0:
#             num.append(i)
#     return num
#
# print(type_num(ls))

# #10
# ls = [[1,2,3,4], [5,6,7,8], [9,10,11,12]]
# ind = int(input())
# def ret_mat(ls, ind):
#     a = []
#     for i in range(len(ls)):
#         a.append(ls[i][ind-1])
#     return a
# print(ret_mat(ls, ind))

# #11
#
# st = "hello 10 120 1 world"
# def num_in_str(st):
#     a = []
#     st = st.split()
#     for i in st:
#         if str(i).isdigit():
#             a.append(i)
#     return a
# print(num_in_str(st))











# #12
# clas = [[], []]
# students = []
# marks = []
# while True:
#
#     cm = input("add, remove, list, exit, add_mark: ")
#
#     if cm == "exit":
#         break
#
#     elif cm == "add":
#         name = input("введите имя студента:")
#         clas_s = int(input("введите класс студента(1, 2)"))
#         clas[clas_s-1].append(name)
#         marks.append([])
#
#
#
#
#     elif cm == "remove":
#         name = input("введите имя ученика:")
#         ind = int(input("введите номер студента:"))
#         if name in students:
#             students.pop(name)
#             marks[ind-1].pop()
#
#         else:
#             print("студент не найден")
#
#     elif cm == "list":
#         for i in students.keys():
#             print(f"{i} - {students[i]}, {marks}")
#     elif cm == "add_mark":
#         ind = input("введите имя студента:")
#         if ind not in students:
#             print("нет студента")
#         else:
#
#
#     else:
#         print("команда не найдена!")































