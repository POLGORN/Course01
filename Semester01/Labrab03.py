# # # 0 # # #
def task01():
    n = int(input())
    m = n
    z = 1
    if configuration == 1:
        n = 1
    while n != 0:
        if configuration == 2:
            print( 'X' * m )
            n -= 1
        else:
            if z % 2 == 0:
                print( '-' * m )
                n -= 1
                z += 1
            else:
                print( 'X' * m )
                n -= 1
                z += 1

def task02():
    n = int(input())
    m = ''
    a = [i for i in range(1, (n ** 2) + 1)]
    for i in a:
        if i % 2 == 0:
            m += '-'
        else:
            m += 'X'
    b = m[:n]
    c = m[1:n + 1]
    if configuration == 1:
        print((b + '\n') * n) 
    else:
        for i in range(1, n + 1):
            if i % 2 == 0:
                print(c)
            else:
                print(b)

def task03():
    n = int(input())
    for i in range (0, n):
        m = n - 1
        if configuration == 1:
            i, m = m, i
        print('-' * m + 'X' + '-' * i)
        n += -1

def task04(arr, size):
    arrs = []
    p = 2
    if configuration == 1:
        while len(arr) > size:
            pice = arr[:size]
            arrs.append(pice)
            arr = arr[size:]
        arrs.append(arr)
        return arrs
    else:
        while len(arr) > size:
            if p % 2 == 0:
                pice = arr[:size]
                arrs.append(pice)
                arr = arr[size:]
                p += 1
            else:
                pice = arr[:size]
                picee = pice[::-1]
                arrs.append(picee)
                arr = arr[size:]
                p += 1
        if mod % 2 == 0:
            arrs.append(arr[::-1])
        else:
            arrs.append(arr)
        return arrs

def task06():
    for с in b:
        print(' '.join(map(str, с)))

# # # ПЕРВОЕ ЗАДАНИЕ # # #
# configuration = 1
# task01()

# # # ВТОРОЕ ЗАДАНИЕ # # #
# configuration = 2
# task01()

# # # ТРЕТЬЕ ЗАДАНИЕ # # #
# configuration = 3
# task01()
        
# # # ЧЕТВЁРТОЕ ЗАДАНИЕ # # #
# configuration = 1
# task02()

# # # ПЯТОЕ ЗАДАНИЕ # # # 
# configuration = 1
# task03()

# # # ШЕСТОЕ ЗАДАНИЕ # # #
# configuration = 2
# task03()

# # # СЕДЬМОЕ ЗАДАНИЕ # # #
# configuration = 2
# task02()

# # # ВОСЬМОЕ ЗАДАНИЕ # # #
# def task05():
#     n = int(input())
#     m = '1'
#     for i in range(2, n + 2):
#         print(m)
#         m = m + ' ' + str(i)
# task05()

# # # ДЕВЯТОЕ ЗАДАНИЕ # # #
# n = int(input())
# configuration = 1
# mod = 1
# a = [i for i in range(1, n**2 + 1)]
# b = task04(a, n)
# task06()

# # # ДЕСЯТОЕ ЗАДАНИЕ # # #
# n = int(input())
# configuration = 2
# mod = n
# a = [i for i in range(1, n**2 + 1)]
# b = task04(a, n)
# task06()
