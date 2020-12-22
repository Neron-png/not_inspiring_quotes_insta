from PIL import Image, ImageDraw, ImageFont
import textwrap
import random
from insta_upload import upload

def compose(content,bot):


    # Pick a random background image #
    template = "template_" + str(random.randrange(0, 5)) + ".png"
    ##################################


    # Add text to image #
    img = Image.open(template)
    img = img.convert("RGB")
    para = textwrap.wrap(content, width=22)

    MAX_W, MAX_H = 512, 512

    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("Chicken_Quiche.ttf", 36)

    current_h, pad = 150, 10
    for line in para:
        w, h = draw.textsize(line, font=font)
        draw.text(((MAX_W - w) / 2, current_h), line, font=font, fill="black")
        current_h += h + pad

    img.save('upload.jpg', format='JPEG', quality=100)

    ####################################
    
    upload(bot)
