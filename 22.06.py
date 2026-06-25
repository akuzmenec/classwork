# st = [1,2,3,4,5]
# print(st[0]+st[1])
# for i in range(5):
#     print(st[i], end=" ")
#
# st = [4,5,3,4,3,4,2,4,]
# for i in range(7, -1, -1):
#
#     print(st[i], end="")
# st = [4,5,3,4,3,4,2,4,]
# max = st[0]
# min = st[0]
# ind_ma = 0
# ind_mi = 0
# for i in range(1,4):
#     if st[i] > max:
#         max = st[i]
#         ind_ma = i
#     if st[i] < min:
#         min = st[i]
#         ind_mi = i
# print(f"максимальное число:{max}, индекс:{ind}")
# print(f"минимальное число:{max}, индекс:{ind}")
# print(max)
# st = [4,5,3,4,3,4,2,4,]
# max = st[0]
# for i in range(1,len(st)):
#     if st[i] > max:
#         max = st[i]
# print(max)

# st[1] = 22
#
# ls = [12,13,25]
#
# for i in range(len(ls)):
#     if ls[i]%2 == 0:
#         print(i,end="")
# ls = [1,2,3,4,5]
# for i in range(len(ls),-1,-1):
#     print(ls[i])
# ls1 = [1,2,3,4,5,4,5,6]
# for i in range(len(ls1)):
#     flag = True
#     for j in range(len(ls1)):
#         if i == j:
#             continue
#         if ls1[0] == ls1[j]:
#             flag = False
#             break
#     if flag:
#         print(ls1[1], end=" ")
# ls1 = [1,2,3,4,5,4,5,6]
# for i in range(len(ls1)):
#     flag = True
#     for j in range(i):
#         if ls1[i] == ls1[j]:
#             flag = False
#             break
#     if flag == False:
#         continue
#     for j in range(i+1, len(ls1)):
#         if ls1[i] == ls1[j]:
#             print(ls1[i], end=" ")
#             break
#
# ls1 = [1,2,3,4,5,4,5,6]
# ls2 = [1,2,3,4,5,4,5,6]
#
#
# if len(ls1) != len(ls2):
#     flag = False
# else:
#     flag = True
#     for i in range(len(ls1)):
#         if ls1[i] != ls2[i]:
#             flag = False
#             break
# print(flag and "равны" or "разные")
#















