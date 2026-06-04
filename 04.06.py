

#1
num1 = int(input())
num2 = int(input())

if num1 > num2:
    print(num1)
elif num1 == num2:
    print(f"{num1} = {num2}")
else:
    print(num2)


#2
s = int(input())
t = int(input())
print("middle speed:", s/t)


#3
num3 = int(input())
a = num3 % 10
b = (num3//10) % 10
c = num3//100
print(f"{a}{b}{c}")