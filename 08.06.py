#1
a = int(input())
b = int(input())
c = int(input())

if (a > c) and (a > b):
    print(a)
elif (b > a) and (b > c):
    print(b)
elif (c > a) and (c > b):
    print(c)

#2
d = int(input())
if d % 2 == 0:
    print("yes")
else:
    print("no")

#3
e = int(input())

if (e//10 == 3) or (e % 10 == 3):
    print("yes")
else:
    print("no")

#4
f = int(input())

if (f > 10) and (f < 20):
    print("yes")
else:
    print("no")
#5

g = int(input())
h = int(input())

if (g % 3 == 0) and (h % 3 == 0):
    print("yes")
else:
    print("no")