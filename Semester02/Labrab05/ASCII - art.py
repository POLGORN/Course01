# Она нам немного пригодится для вычислений
import math
# Она для самой работы с фото
from PIL import Image, ImageDraw, ImageFont

# Основываясь на особенности пикселя(h) дает конкретный символ
def getChar(inputInt):
    return charArray[math.floor(inputInt * interval)]


# Для светлых фото
# chars = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\\|()1{}[]?-_+~<>i!lI;:,\"^`'. "[::-1]

# Для темных фото
chars = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\\|()1{}[]?-_+~<>i!lI;:,\"^`'. "

# Просто кусок с переменными
charArray = list(chars)
charLength = len(charArray)
interval = charLength / 256

# Значение детализации(увеличивай для маленькихa фото, уменьшай для больших(больше 0.5 лучше не выставлять))
scaleFactor = 0.35

# Размер символов чем меньше значение тем больше символы и наоборот)
# Если работать с ними, то лучше увеличить и уменьщать в % соотношении(за основу oneCharWidth = 10, oneCharHeight = 18)
oneCharWidth = 9
oneCharHeight = 16

# Открываем саму картинку
im = Image.open(input())

# Указываем какой шрифт и размер шрифта хочется для ASCII-art-a 
fnt = ImageFont.truetype('C:\\Windows\\Fonts\\lucon.ttf', 15)

# Чутка шаманим с размерами
width, height = im.size
im = im.resize((int(scaleFactor * width), int(scaleFactor * height * (oneCharWidth/oneCharHeight))), Image.NEAREST)
width, height = im.size
pix = im.load()

# Тут создаём саму картинку указывая параметры(режим - размер - цвета)
outputImage = Image.new('RGB', (oneCharWidth * width, oneCharHeight * height), color = (0, 0, 0))
# Создаем обьект на котором будет жить картинка
d = ImageDraw.Draw(outputImage)

# Создаем текстовый ASCII-art
text_file = open("Output.txt", "w")

# Заполняем наши .txt и .png файлы по-пиксельно
for i in range(height):
    for j in range(width):
        r, g, b = pix[j, i]
        h = int(r / 3 + g / 3 + b / 3)
        pix[j, i] = (h, h, h)
        text_file.write(getChar(h))
        d.text((j * oneCharWidth, i * oneCharHeight), getChar(h), font = fnt, fill = (r, g, b))
    text_file.write('\n')

# Сохраняем нашу .png картинку на память
outputImage.save('output.png')

# Если очень сильно хочется картинку в высокой детализации, 
# то стоит разбить программу на класс с методами и через
# компилятор Numba всё вкусно сделать,
# но я не хочу вводить себя в депрессию делая это, может быть позже.

# Размером символов и детализацией можно манипулировать для увеличения/уменьшения насыщенности и
# затемнённости/осветлённости, а так же, как не странно, для детализации,
# по небольшому личному опыту могу сказать что лучше всего фото получается при -
# scaleFactor = 0.15 или 0.35-0.40 + oneCharWidth = 9 + oneCharHeight = 16,
# однако всё это можно поправить и исправить без проблем.

