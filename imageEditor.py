from PIL import Image, ImageDraw, ImageFont
from io import BytesIO
import textwrap
import random
import string
import sentencesAI


def draw_multiple_line_text(image, text, font, text_start_height):
    draw = ImageDraw.Draw(image)
    image_width, image_height = image.size
    y_text = text_start_height
    lines = textwrap.wrap(text, width=15)
    for line in lines:
        line_width, line_height = font.getsize(line)
        draw.text(((image_width - line_width) / 2, y_text), 
                  line,(0,0,0), font=font)
        y_text += line_height




def edit_image():
    newAdvice = sentencesAI.get("advice")
    
    image = Image.open("./background/"+str(random.randint(0,74))+".jpg")
    f = open("./fonts/RobotoSlab-Bold.ttf", "rb")
    bytes_font = BytesIO(f.read())
    font = ImageFont.truetype(bytes_font, 45)

    text_start_height = 150
    draw_multiple_line_text(image, newAdvice, font, text_start_height)

    filename = ''.join(random.choice(string.ascii_lowercase) for i in range(16))

    image.save('./ai.uttutu/image.jpg')
    image.save('./all-images/'+filename+'.jpg')


if __name__ == "__main__":
    edit_image()