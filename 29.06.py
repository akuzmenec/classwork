
# ls = [1,2,3,4,5]
#
# for i in range(len(ls)):
#     if ls[i] < 0:
#         ls[i] *= -1
# print(ls)

# ls = [1, 2, 3, 4, 5]
# for i in range(len(ls)//2):
#
#     ls[i], ls[len(ls)-(i+1)] = ls[len(ls)-(i+1)], ls[i]
# print(ls)


# names = ["joe", "mark", "james"]
#
# flag = True
# for i in range(1,len(names)):
#     if len(names[i]) != len(names[0]):
#         flag = False
#         break
# print(flag and "все равны" or "не равны")

# ls = ["ca", "ba", "hb"]
#
# for i in range(len(ls)):
#     if ls[i][len(ls[i])-1] == "a":
#         print(ls[i])

# st = [[1, 2], [3, 4]]
# for i in range(len(st)):
#     for j in st[i]:
#         print(j, end=" ")
#     print()



# m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# sum = 0
# for i in range(len(m)):
#     for j in m[i]:
#         sum += j
#         print(j, end="\t")
#     print("|", sum)
# print("----------")
#
# result = 0
# for i in range(len(m[0])):
#     sum_1 = 0
#     for j in range(len(m)):
#         sum_1 += m[j][i]
#
#     print(sum_1, end="\t")
#     result += sum_1
# print("|", result)

