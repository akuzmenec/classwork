from random import randint

#
# st = "hello world 123"
# k = 0
# for i in st.split(" "):
#     if i.isalpha():
#         k += 1
#
# print(k)
#
#
# print(st.count(" ")+1)
#
# ls = []
#
# n = int(input())
#
# for i in range(n):
#     ls.append(randint(1, 100))
#
# print(ls)

ls1 = [3, 1, 2, 3, 4, 3, 5, 3, 3]
a = 3
# def rm_ls(ls1, a):
#     k = 0
#     s = len(ls1)
#     while k<s:
#         if ls1[k] == a:
#             ls1.remove(a)
#             s -= 1
#             k -= 1
#         k += 1
#
# rm_ls(ls1, a)
#
# print(ls1)


# def rm_all_pop(ls1, a):
#
#     k = 0
#     s = len(ls1)
#     while k < s:
#         if ls1[k] == a:
#             ls1.pop(k)
#             s -= 1
#             k -= 1
#         k += 1
#
# rm_all_pop(ls1, a)
#
# print(ls1)


students = []

students_marks = []


while True:
    cm = int(input("1 - добавить ст, 2 - удалить ст, 3 - добавить оценки ,4 - исправить оценки ,5 - вывести инф, 6 - выход"))
    if cm == 1:
        name = input("введите имя: ")
        students.append(name)
        students_marks.append([])
    elif cm == 2:
        ind = int(input("введите номер ст:"))
        if 1<=ind<=len(students):
            students.pop(ind-1)
        else:
            print("нет такого ст")
    elif cm == 3:
        ind = int(input("введите номер студента:"))
        mark = int(input("введите оценку:"))

        students_marks[ind - 1].append(mark)
    elif cm == 4:
        print(students_marks)
        inds = int(input("введите номер:"))
        indn = int(input())

        if 1<=inds<=len(students):
            students.pop(inds-1)
        else:
            print("нет такого ст")
        mark = int(input("введите оценку:"))
        students_marks[inds][indn] = mark

    elif cm == 5:
        for i in range(len(students)):
            print(f"студент:{students[i]}, оценки:{students_marks[i]}")
    else:
        break


















