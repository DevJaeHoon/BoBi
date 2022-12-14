from threading import Timer
from time import sleep
import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306

from PIL import Image
from PIL import ImageDraw


RST = None
disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST)

disp.begin()
disp.clear()
disp.display()

def always():
    global disp
    im = Image.new('1', (128,64), 0) 
    draw = ImageDraw.Draw(im)

    box = (42,0,86,64)
    draw.ellipse(box,fill = 1)

    # Display image.
    disp.image(im)
    disp.display()

def heart() :
    global disp
    image = Image.open('heart.png').convert('1')

    disp.image(image)
    disp.display()
    sleep(3)
    always()

def record() :
    global disp
    image = Image.open('record.png').convert('1')
    disp.image(image)
    disp.display()

def msg() :
    global disp
    image = Image.open('msg.png').convert('1')
    disp.image(image)
    disp.display()

def sit() :
    global disp
    im = Image.new('1', (128,64), 0) 
    draw = ImageDraw.Draw(im)
    draw.line((4,60,64,0),fill=1, width=10)
    draw.line((64,0,124,60),fill=1, width=10)
    disp.image(im)
    disp.display()

def down() :
    global disp
    im = Image.new('1', (128,64), 0) 
    draw = ImageDraw.Draw(im)
    draw.line((20,32,108,32),fill=1, width=10)
    disp.image(im)
    disp.display()

def speak() :
    global disp
    image = Image.open('speak.png').convert('1')
    disp.image(image)
    disp.display()

def emotion() :
    global state, timer
    if(state == 'always') :
        always()
    elif(state == 'heart') :
        heart()
    elif(state == 'record') :
        record()
    elif(state == 'msg') :
        msg()
    elif(state == 'sit') :
        sit()
    elif(state == 'down') :
        down()
    elif(state == 'speak') :
        speak()
    
    timer = Timer(0.1, emotion)
    timer.start()
state = None
timer = None
always()
emotion()
    