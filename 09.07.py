# st = "hello"
#
# st2 = ""
#
# for i in st:
#     if i != "h":
#         st2 += i
#
# print(st2)
# print(st[0:6:1])
# print(st[:-1])
#
# ls = ["hello", "kasdvna", "joy"]
#
# for i in ls:
#     if i[::-1] == "olleh":
#         print(i)
# ls1 = ["алекс", "никола"]
# glass = "аеёиоуыэюя"
#
# for i in ls1:
#     if i[0] in glass:
#         print(i)
#
# print(glass[glass.find("о"):])
# begin end
# st = "begin hello end"
# def ret_st(st):
#
#      return st[st.find("begin") + 5:st.find("end")]
#
# print(ret_st(st))
#
# #### если в find такого элемента нет то выводится -1
# #### find/rfind
# #### https://pythonworld.ru/tipy-dannyx-v-python/stroki-funkcii-i-metody-strok.html
#
# print(st.replace("begin", "a"))
#
# print(st.split(" "))
#
# st = "если сделал уроки и помыл посуду можешь идти гулять!"
# st2 = ""
# ls = st.split(" ")
# for i in ls:
#      if i[-1] == "л":
#           i += "a"
#      st2 += i + " "
# print(st2.strip())

# st = "апельсин мандарин апельсин тоже фрукт что и мандарин"
#
# print(list(set(st.split(" "))))

st ='1 2 3 5 sgh'
k = 0
for i in st:
    if i.isdigit():
        k += 1
print(k)























