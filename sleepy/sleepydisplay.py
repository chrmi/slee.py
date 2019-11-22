from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import Adafruit_SSD1306

import sleepystate

RST = 24 

disp = Adafruit_SSD1306.SSD1306_128_32(rst=RST)

disp.begin()
disp.clear()
disp.display()

width = disp.width
height = disp.height
image = Image.new('1', (width, height))

draw = ImageDraw.Draw(image)

draw.rectangle((0,0,width,height), outline=0, fill=0)

font = ImageFont.truetype('/home/pi/slee.py/pixelmix/pixelmix.ttf', 6)
boldFont = ImageFont.truetype('/home/pi/slee.py/pixelmix/pixelmix_bold.ttf', 8)

def update():
    draw.rectangle((0,0,width,height), outline=0, fill=0)
    draw.text((0, 2), str(sleepystate.getPreviousTrack()), font=font, fill=255)

    if not sleepystate.isPaused() and sleepystate.getSelectedTrack() == sleepystate.getPlayingTrack():
        draw.text((0, 12), "-", font=boldFont, fill=255)

    draw.text((9, 11), str(sleepystate.getSelectedTrack()), font=boldFont, fill=255)
    draw.text((0, 24), str(sleepystate.getNextTrack()), font=font, fill=100)
    disp.image(image)
    disp.display()
