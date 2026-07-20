#процедура не принимает данные в отличии от функции

# def calc(a, b, c=5):
#     print(a+b+c)
# calc(1, 2)
#
#
# def test(a):
#     return a
#     return a
# print(test(5))


### рекурсивная функц


# def rec(ls, ind=0):
#
#     print(ls[ind])
#     if ind < len(ls) - 1:
#         rec(ls, ind + 1)
#
#     print(ind)
# print(rec([1, 2, 3, 4, 5]))




#
# def fac(n):
#     if n > 1:
#         return n * fac(n-1)
#     else:
#         return 1
# print(fac(5))



#
#
#
#
# # бинарный поиск
#
#
# ls = [5, 4, 3, 2, 1]
# ls.sort()
#
# n = 4
#
# ind1 = 0
# ind2 = len(ls) - 1
# #сложности алгоритмов
#
#
# st = "hello pl sdf lf lf  "
#
# def con(st):
#     a = set()
#     ls = st.split()
#     for i in ls:
#         if len(i) < 3:
#             a.add(i)
#     return a
#
#
# print(con(st))


# ls1 = [1, 2, 3, 4]
# ls2 = [4, 5, 1, 3]
# print(set(ls1).intersection(set(ls2)))
#
# def unic_all(ls1, ls2):
#     a = set()
#     for i in ls1:
#         if i in ls2:
#             a.add(i)
#     return a
#
# print(unic_all(ls1, ls2))



dic1 = {"anny": 21, "joy": 22, "bob": 33}
dic2 = {"anny": 21, "bill": 22, "bob": 33}
dic3 = {}

print(dic3)








