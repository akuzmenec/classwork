# file = open("test1.txt", "a")
# text = ["str1", "str2"]
# try:
#     for i in text:
#         file.write(i+"\n")
#
# except Exception:print("ex")
#
# finally: file.close()
#
# with open("test1.txt", "a") as file:
#     file.read(78)
# print("asdjc")



# with open("test1.txt", "r", encoding="UTF - 8") as file:
#     s = 0
#     for i in file.readlines():
#         ls = i.split((","))
#         if ls[2][-1:]=="\n":
#             ls[2]=ls[2][:-1]
#     print(f"{ls[0]}: {int(ls[1]) * int(ls[2])}")
######kwargs

PATH = "test1.txt"
def add_product(**kwargs):
    with open(PATH, "r", encoding="UTF - 8") as file:
        pr = dict()
        for i in file.readlines():
            ls = i.split(",")
            pr[ls[0]] = ls[1]
        pr[kwargs['name']] = f"{kwargs['price']}\n"
    with open(PATH, "w", encoding="UTF - 8") as file:
        for key, value in pr.items():
            file.write(f"{key}, {value}")


# def show():
#     with open(PATH, "w", encoding="UTF - 8") as file:
#
#         for i in file.readlines():
#             ls = i.split(",")
#             print(f"{ls[0]} - {ls[1]}", end="")

add_product(name = 'котел', price = '15000')

###вывести отфильтрованные товары по цене или алфавиту и тд
# def sort_pr()
#