while True:
    kk = int(input('Give a number: '))
    ww = int(input('Give another number: '))
    list1 = [1, 2, 3]
    list2 = [1, 2, 3]
    numba = (sum([kk * num for num in list1]) + sum([ww * num for num in list2]))

    if numba == 66:
        numba = 3 + numba
        quit(f'{numba}nice')
    elif numba == 420:
        quit('Go smoke one for me!')
    else:
        print(numba)
