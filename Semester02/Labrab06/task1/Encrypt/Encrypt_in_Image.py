from PIL import Image, ImageDraw # Нужна для работы с картинкой
from random import randint # Нужна для выбора случайного числа

def Encrypt_in_Image():
    keys = [] # Здесь будут записаны координаты пикселей в которых шифровали текст
    img = Image.open(input('В какую картинку изволите шифровать? -> ')) # Вводим картинку
    draw = ImageDraw.Draw(img) # Создаём обьект для рисования
    width = img.size[0] # Ширина
    height = img.size[1] # Высота
    pix = img.load() # Загружаем "пиксельные данные"
    f = open('keys.txt', 'w') # Создаём текстовый файл где будут ключи

    for elem in ([ord(elem) for elem in input('Что за секрет? -> ')]): # Этим циклом мы кодируем каждый символ
        key = (randint(1, width), randint(1, height)) # Сначала наугад ткнем пальцем на пиксель картинки
        g, b = pix[key][1:3] # Узнаем его зелёный и синий параметр 
        draw.point(key, (elem, g, b)) # Заменим его красный элемент на ord(elem)
        f.write(str(key)+'\n') # Напишем координаты пикселя который только что использовали

    img.save('secret.png', 'PNG') # Сохраним
    f.close() # Закроем


Encrypt_in_Image() # Запустим
