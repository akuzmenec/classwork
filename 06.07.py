# def min(ls):
#     min = ls[0]
#     ind = 0
#     for i in range(len(ls)):
#         if ls[i] < min:
#             min = ls[i]
#             ind = i
#     return ind
#
# ls1 = [1,2,3,4,5]
#
# print(min(ls1))
def swap(ls, ind1, ind2):
    ls[ind1], ls[ind2] = ls[ind2], ls[ind1]
# ### bubble switch
# ls = [9, 8, 7, 6, 5]
#
# for j in range(len(ls)-1):
#     flag = False
#     for i in range(len(ls) - 1 - j):
#         if ls[i] > ls[i+1]:
#             swap(ls, i, i+1)
#             flag = True
#     if not flag:
#         break
#
# print(ls)
# ###
# ls = [9, 8, 7, 6, 5]
# # def ins_sert(ls):
#
# for i in range(1, len(ls)):
#     for j in range(i, 0, -1):
#         if ls[j] < ls[j-1]:
#             swap(ls, j, j-1)
#         else:
#             break
# print(ls)

a = 5
# def name_function():
#     global a
#     print(a, end=" ")
#     a -= 1
#     if a > 0:
#         name_function()
#     print(a, end=" ")
# name_function()

# s = 0
#
# def summa():
#     global s
#     a = int(input())
#     s += a
#     if a!=0:
#         return summa()
#     return s
#
# print(summa())
#
# def summa(s=0):
#     a = int(input())
#     s += a
#     if a!=0:
#         return summa(s)
#     return s
#
# print(summa())






