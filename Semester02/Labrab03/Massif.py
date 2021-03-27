# # # 1 # # #
'''
Из списка чисел берёт любое четное
'''
# def alpha():
#     for beta in input().split():
#         if int(beta) % 2 == 0:
#             return beta
# print(alpha())


# # # 2 # # #
'''
Из списка чисел печатает все нечётные
'''
# print(*list(filter(lambda x: x % 2 == 1, list(map(int, input().split())))), sep=" ")


# # # 2 # # #
'''
Отсортировать список чисел по убыванию(Большее -> меньшее)
'''
# print(*sorted(map(int, input().split()), reverse=True), sep=" ")


# # # 3 # # # 
'''
Из списка надо выдать сумму ТРЁХ наименьших чисел
'''
# print(sum(sorted(list(map(int, input().split())))[:3]))


# # # 4 # # #
'''
Из списка надо выдать минимальное число оканчивающееся на 3
'''
# gamma = []
# for inp in range(int(input())):
#     delta = input()
#     gamma.append(delta) if int(''.join([alpha for alpha in delta][-1])) == 3 else ...
# print(min(map(int, gamma)))


# # # 5 # # #
'''
Даётся список в разброс 1-100 где пропущен 1 число, надо найти за 1 секунду в функциональном стиле
'''
# import functools
# print(5050 - (functools.reduce(lambda a,b : a + b, map(int, input().split()))))


# # # 6 # # #
'''
Даётся список в разброс 1-100 где повторяется число, условия те же
'''
# import functools
# print((functools.reduce(lambda a,b : a + b, map(int, input().split()))) - 5050)


# # # 7 # # #
'''
Даны числа у всех есть пары кроме 1 найти 1
'''
# alpha = input().split()
# print(min(set(alpha), key=lambda x: alpha.count(x)))


# # # 8 # # # 
'''
В 1 строчке даётся номер в рейтинге, в следующих 20 языки программирования;рейтинг
пользователь должен ввести номер рейтинга, а программа выдать язык
'''
# import operator

# def delta():
#     return sorted(gamma.items(), key=operator.itemgetter(-1), reverse=True)


# alpha = int(input())
# gamma = {}
# for num in range(20):
#     beta = input().split(';')
#     gamma[beta[0]] = float(beta[1])
# print(delta()[alpha - 1][0])
