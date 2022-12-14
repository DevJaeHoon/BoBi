from threading import Timer,Lock    
import mysql.connector
import sensor_oled
from time import sleep
import RPi.GPIO as GPIO
from voice_speaker import Speaker

def up():
    global closeness, timer, speaker
    
    dotouch = GPIO.input(tilt_pin)  # 터치 누르면 1 안누르면 0 출력
    if dotouch : 
        closeness += 50
        print(closeness)
        if closeness % 100 != 0 :
            sensor_oled.state = 'heart'
            sleep(3)
            sensor_oled.state= 'always'
        sleep(3)   
        

    timer = Timer(0.1, up)
    timer.start()
def check():
    global timer2
    if(speaker.is_new_story_available()):
        sensor_oled.state = "sit"
        speaker.new_story_available()
        sensor_oled.state = "always"
    timer2 = Timer(1, check)
    timer2.start()

def polling():
    global cur, db, closeness
    lock.acquire()  
    cur.execute("select * from bobi_robot order by robot_id desc limit 1")
    for (robot_id, exp, level) in cur:
        closeness = exp 

    db.commit()
    lock.release()
    cur.close()
    db.close()

db = mysql.connector.connect(host='[server ip]', port = '3306', user='pjt_bobi', password='[server pw]', database='bobi', auth_plugin='mysql_native_password')
cur = db.cursor()
timer = None
timer2 = None
lock = Lock()
closeness = 500
tilt_pin = 4 #터치 센서의 경우 센서만 바꾸면 됨
GPIO.setmode(GPIO.BCM)
GPIO.setup(tilt_pin, GPIO.IN)
speaker = Speaker()

check()
polling()
up()

    
     
            
        
   
     
            
        
