###https://pythonworld.ru/tipy-dannyx-v-python/mnozhestva-set-i-frozenset.html
#
from random import randint
# a = []
# c = []
#
# n = int(input())
#
# def add_num(ls):
#     for i in range(n):
#         b = randint(1, 9)
#         if b not in ls:
#             ls.append(b)
#
# add_num(a)
# add_num(c)
#
# a = set(a)
# c = set(c)
#
# print(a, c)
#
# s = a.intersection(c)
# print(len(s))
#
# print(s > a.difference(c) and "intersection > difference" or "difference > intersection")
#
# print(((len(a) + len(c) - len(s)) and "difference > intersection" or "intersection > difference"))
#
#
# products = {"name": "яблоки", "printce": 1234, "count": 134, "colors": ["красный", "синий"]}
#
# print(products["name"])
# for i in products.keys():
#     print(f"{i} - {products[i]}")
#
#
#
# products["name"] = "банан"
#
#
# products["category"] = "акцессуары"
#
#
# print(products)

disciplines = ["eng", "math", "lit", "rus"]

def show(dict1):
    for i in dict1.keys():
        print(f"{i} - {dict1[i]}")

def marks(ls):
    dict = {}
    max = 0
    for i in ls:
        dict[i] = []
        for j in range(randint(3, 9)):
            dict[i].append(randint(2, 5))
    return dict

def avg(list):
    sum = 0
    for i in list:
        sum +=1
        return sum/len(list)

# def best_name(dict):
#     max = 0
#
#     for i in dict.keys():
#         marks = avg(dict[i])
#         if max < marks:
#             max = marks
#             dict_name = i
#
#     return dict_name
#
#
# def best_count(dict):
#     max = 0
#
#     for i in dict.items():
#         marks = len(dict.items())
#         if max < marks:
#             max = marks
#             dict_name = i
#
#     return dict_name


marks(disciplines)



def more_then_3(dict):
    dict_name = []
    for i in dict.keys():
        mark = avg(dict(dict[i]))
        if mark > 3:
            dict_name += i
    return dict_name

print(more_then_3(dict))






































