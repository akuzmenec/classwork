from random import randint

#1-к
#2-н
#3-б

k = 0
w = 0
l = 0


while k != 3:
    ch = int(input("если вы хотите играть с игроком введите 0. Иначе 1"))
    if ch == 0:
        c = int(input("ход игрока:"))
    else:
        c = randint(1, 3)
    y = int(input("ваш ход:"))
    while y > 3 or y <= 0:
        y = int(input("числотвведено неправильно. Попробуйте еще раз:"))
    if c == y:
        print("ничья")
    elif (c == 1 and y == 3) or (c == 2 and y == 1) or (c == 3 and y == 2):
        print("вы победили в этом раунде!")
        w += 1
    else:
        print("вы проиграли в этом раунде!")
        l += 1

    if c == 1:
        print("у противника был камень!")
    elif c == 2:
        print("у противника были ножницы!")
    else:
        print("у противника была бумага!")

    k += 1
    if k == 3:
        print("игра завершилась")
        print(f"выйграно раундов: {w}, проиграно: {l}")

        if w > l:
            print("вы выйграли!")
        else:
            print("вы проиграли!")

        n = int(input("Если хотите выйти введите 0"))

        if n == 10:
            k = 0
        else:
            break


