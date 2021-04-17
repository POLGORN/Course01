from PIL import Image
from re import findall # Штука которая используется для поиска всех непересекающихся совпадений в шаблоне что бы это ни значило

def Decrypt_of_Image():
    a = [] # То куда мы поместим наш итог
    keys = [] 
    img = Image.open(input('И что же предстрить декодить? -> '))
    pix = img.load()
    f = open(input('Прошу, введите ключ -> '),'r')
    y = str([line.strip() for line in f]) # Просто считывает ключи

    for i in range(len(findall(r'\((\d+)\,', y))): # Запускает цикл длинной в кол-во закодированных символов
        keys.append((int(findall(r'\((\d+)\,', y)[i]), int(findall(r'\,\s(\d+)\)',y)[i]))) # Практически дублируем ключи просто приводя их в удобный вид
    for key in keys: 
        a.append(pix[tuple(key)][0]) # Берём первый параметр пикселя(red) который мы и закодировали
    return ''.join([chr(elem) for elem in a]) # Преобразовываем в нормальный текст


print('Было расшифровано следующее -> ', Decrypt_of_Image())
