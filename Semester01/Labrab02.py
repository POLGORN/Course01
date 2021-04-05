# # # ПЕРВОЕ ЗАДАНИЕ # # #
# n = input()
# m = list(n)
# acc = 0
# for item in m:
#     acc += int(item)
# print(acc)

# # # ВТОРОЕ ЗАДАНИЕ # # #
# a = int(input())
# if a & ( a - 1 ):
#     print( "NO" )
# else:
#     print( "YES" )

# # # ТРЕТЬЕ ЗАДАНИЕ # # #
# n = int(input())
# m = 8
# newn = ''
# while n > 0:
#     newn = str(n % m) + newn
#     n //= m
# print(newn)

# # # ЧЕТВЕРТОЕ ЗАДАНИЕ # # #
# my_file = open('some.txt', 'w')
# n = int(input())
# a, b = 2, 1
# for i in range(1, n+1):
#     if i % 2 == 0:
#         y = a / b
#         my_file.write(str(y) + '\n')
#         a += 2
#     else:
#         z = a / b
#         my_file.write(str(z) + '\n')
#         b += 2
# my_file.close()
# acc = 0
# for i in open('some.txt'):
#     acc += float(i)
# print (acc)

# # # ПЯТОЕ ЗАДАНИЕ # # #
# import math
# g = int(input())
# q = float(input())
# x = math.pi/180 * g
# p = 1 
# z = 1 
# sin_x = 0 
# step = q + 1
# while abs(step) > q:
#     step = z * (x**p / math.factorial(p))
#     p += 2
#     z = -z
#     sin_x += step
# print('sin = %.3f' % sin_x)

# # # ШЕСТОЕ ЗАДАНИЕ # # #
# n = int(input())
# m = n - 1
# for i in range(0, n):
#     print(' ' * m + 'X' * i + 'X' + 'X' * i)
#     m += -1
