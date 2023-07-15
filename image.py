from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

#загрузка фонового изображения
background = Image.open('photo/banner.png')

#загрузка и изменеине размера фото персонажа
picture = Image.open('photo/hutao.webp')
width, height = (picture.size)
newHeight = 500
newWidth = width * newHeight // height
size=(newWidth,newHeight)
pictureResize = picture.resize(size)
Image.Image.paste(background, pictureResize, (42, -20), mask=pictureResize)

#наложение элемента
pictureelem = Image.open('photo/piro.png')
width, height = (pictureelem.size)
newHeight = 70
newWidth = width * newHeight // height
size=(newWidth,newHeight)
pictureResize = pictureelem.resize(size)
Image.Image.paste(background, pictureResize, (6, 205), mask=pictureResize)

#наложение текста
draw = ImageDraw.Draw(background)
font = ImageFont.truetype("font/Default_JP.ttf", 35)
draw.text((45, 210),"Ху Тао",(255,255,255),font=font)

#наложение звёздочек
picturestar = Image.open('photo/5star.png')
width, height = (picturestar.size)
newHeight = 20
newWidth = width * newHeight // height
size=(newWidth,newHeight)
pictureResize = picturestar.resize(size)
Image.Image.paste(background, pictureResize, (60, 250), mask=pictureResize)

background.save('photo/result.jpg', quality=95)