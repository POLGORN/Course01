'''
Кодируем информацию как Цезарь
'''
def code(alph, line, key):
    return ([[alph[x + key] for x in range(len(alph)) if line[i] == alph[x]] for i in range(len(line))])


def cleaner(one):
    clean_code = ''
    for lst in [one[y] for y in range(len(one))]:
        for sm in lst:
            clean_code += sm
    return clean_code


rus = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
nums = '1234567890'
smbs = ':; !&-+=()*/.,'
alph = rus + rus.upper() + nums + smbs

line = 'Опачки Попачки'

key = 4

print(cleaner(code(alph, line, key)))

# Более читаемая версия первой функции(если так вообще можно выразиться)
# def code(alph, line, key):
#     return([
#         [
#         alph[x + key] 
#         for x in range(len(alph)) if line[i] == alph[x]
#         ]
#         for i in range(len(line))
#         ])
