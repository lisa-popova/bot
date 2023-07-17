from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

import os
import sqlite3

dir = os.path.abspath(os.curdir)

sqlite_connection = sqlite3.connect('genshin.db')
cursor = sqlite_connection.cursor()

cursor.execute("SELECT id, name, image, rarity, element FROM pers order by id")

for id, name, image, rarity, element in cursor.fetchall():
    print(name, rarity, image, element)

    #загрузка фонового изображения
    background = Image.open('photo/banner.png').convert('RGBA')
    bgwidth, bgheight = (background.size)

    #загрузка и изменеине размера фото персонажа
    picture = Image.open(dir + image).convert('RGBA')
    width, height = (picture.size)
    newHeight = 500
    newWidth = width * newHeight // height
    size=(newWidth,newHeight)
    offset = bgwidth - newWidth
    pictureResize = picture.resize(size)
    Image.Image.paste(background, pictureResize, (offset, -20), mask=pictureResize)

    #наложение элемента
    pictureelem = Image.open('element/' + element +'.png').convert("RGBA")
    width, height = (pictureelem.size)
    newHeight = 70
    newWidth = width * newHeight // height
    size=(newWidth,newHeight)
    pictureResize = pictureelem.resize(size)
    Image.Image.paste(background, pictureResize, (6, 205), mask=pictureResize)

    #наложение текста
    draw = ImageDraw.Draw(background)
    font = ImageFont.truetype("font/Default_JP.ttf", 35)
    draw.text((45, 210),name,(255,255,255),font=font)

    #наложение звёздочек
    picturestar = Image.open('rarity/' + str(rarity) + 'star' + '.png')
    width, height = (picturestar.size)
    newHeight = 20
    newWidth = width * newHeight // height
    size=(newWidth,newHeight)
    pictureResize = picturestar.resize(size)
    Image.Image.paste(background, pictureResize, (60, 250), mask=pictureResize)

    background.save('pers_banner/' + name + '.png', quality=95, format="png")