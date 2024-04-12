from PIL import ImageDraw
from PIL import Image
from PIL import ImageFont

pic = Image.open('water_marking/image/beach.jpg')

width, height = pic.size
drawing = ImageDraw.Draw(pic)


font = ImageFont.truetype("water_marking/WinterSong-owRGB.ttf", 250)

fill_color = (203,201,201)

watermark_text = "All Rights Reserved"

# x = width / 10 + 10
# y = height - 500

x = width/4 - 50
y = height/2 - 50

position = (x, y)

drawing.text(xy = position, text = watermark_text, font = font, fill = fill_color)

# pic.show()

pic.save('water_marking/image/watermarked_beach.jpg')

watermark_pic = Image.open('water_marking/image/watermarked_beach.jpg')
watermark_pic.show()