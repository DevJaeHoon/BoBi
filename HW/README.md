---
last modified: 2022-08-18
---
# ๐ค HW(robot)
- ๋ก๋ด์์๋ ์์ ์ธ์, ์์ฑ ์ธ์, ์ผ์ ๋ฑ์ ๋ผ์ฆ๋ฒ ๋ฆฌํ์ด์์ ๋ด๋นํ๊ณ  ๋ชจํฐ, LED, ๋ถ์ ๋ ESP32์์ ๋ด๋น
- ๋ก๋ด ์ฌ์ฉ์ ์ํด ๊ธฐ๋ณธ ์ธํ์ ์งํ ํ ํ๋ก์ ํธ ์ธํ ์งํ 
- ESP32๋ฅผ ๋จผ์  ํค๊ณ  ๋ผ์ฆ๋ฒ ๋ฆฌํ์ด๋ฅผ ์ผ์ผ ์ ์๋์
- ์์ธํ ๋ด์ฉ, version ๋ฑ์ [**wiki**](https://lab.ssafy.com/s07-webmobile3-sub2/S07P12A208/-/wikis/home) ํน์ ๊ฐ ๊ธฐ๋ฅ์ requirements.txt ์ฐธ๊ณ 

## โ๏ธ ๊ธฐ๋ณธ ์ธํ
### ๐ฅ How to set RPI
1. ๋ผ์ฆ๋ฒ ๋ฆฌํ์ด์ os๊ฐ ์ค์น๋ sd์นด๋ ์ฐ๊ฒฐ
2. ์๊ฒฉ ์ ์(VNC, mobaxterm ๋ฑ ์ฐธ๊ณ ) ํน์ HDMI ์ผ์ด๋ธ์ ์ง์  ์ฐ๊ฒฐํ์ฌ ๋ผ์ฆ๋ฒ ๋ฆฌํ์ด ์ ์
3. ๋ผ์ฆ๋ฒ ๋ฆฌํ์ด ํฐ๋ฏธ๋์์ ์๋ ฅ(๋ก๋ด ๊ธฐ๋ณธ dependencies ์ค์น)
    ```
    $ sudo git clone https://github.com/waveshare/WAVEGO.git
    $ sudo python3 WAVEGO/RPi/setup.py
    ``` 
4. Completed ๊ฐ ๋จ๊ณ  ๋ผ์ฆ๋ฒ ๋ฆฌํ์ด๊ฐ ์ฌ๋ถํ ๋๋ฉด ์ฑ๊ณต  

[์์ ์ฐธ๊ณ ](https://youtu.be/SlyIttHri6M)

### ๐ How to set Arduino(ESP32)
1. Arduino IDE๋ฅผ ๊ฐ์ธ PC์ ๋ค์ด ๋ฐ๊ธฐ
2. ESP32 ๊ฐ์ธ PC์ ์ ์ ์ผ๋ก ์ฐ๊ฒฐ
3. `file โ Preferences โ Additional Boards Manager URLS` ์ `https://dl.espressif.com/dl/package_esp32_index.json ์๋ ฅ โ OK` ์๋ ฅ
4. IDE ๋ค์ ์์
5. `Tools โ Board โ Boards`์์ ESP32 ๊ฒ์ & Install ํด๋ฆญ
6. ๋ผ์ด๋ธ๋ฌ๋ฆฌ ์ค์น
    - Tools โ Manage Libraries์์ ์๋ ๋ผ์ด๋ธ๋ฌ๋ฆฌ ๊ฒ์ํ์ฌ ์ค์น(Install ํน์ Update)
        - ArduinoJson
        - Adafruit SSD1306
        - Adafruit PWM Servo Driver Library
        - ICM20948 WE
        - INA219 WE
        - Adafruit NeoPixel
7. [๋ก๋ด ๋ฐ๋ชจ์ฝ๋](https://www.waveshare.com/w/upload/3/32/WAVEGO_Demo_Code_%28Arduino%29_220128.zip)๋ฅผ ๋ค์ด๋ฐ์ ์์ถ ํ๊ธฐ
8. `WAVEGO/Arduino/WAVEGO/WAVEGO.ino`๋ฅผ Arduino IDE์์ run
9. `Tools โ Port`์์ ์๋์ด๋ธ๊ฐ ์ฐ๊ฒฐ๋์ด ์๋ ํฌํธ ์ ํ
10. `Tools โ Boards โ ESP32 Arduino โ ESP32 Dev Module` ์ ํ
    - configure ์ธํ ์์
    ```
    Upload Speed: "921600"
    CPU Frequency: "240MHz(WiFi/BT)"
    Flash Frequency: "80MHz"
    Flash Mode: "QIO"
    Flash Size: "4MB(32Mb)"
    ''' Partition Scheme: "Huge APP(3MB No OTA/1MB SPIFFS)"
    PSRAM: "Enabled"'''
    ```
    - Tools โ PSRAM โ Enabled ๋ก ๋์ด ์์ด์ผ ํจ
11. Upload ๋ฒํผ ํด๋ฆญ

[๋ก๋ด ๋ฐ๋ชจ ESP32 ์ฐธ๊ณ ](https://www.waveshare.com/wiki/WAVEGO#Install_Arduino_IDE) 

## โ๏ธ ํ๋ก์ ํธ ์ธํ
- ๊ฐ์ธ PC์์ ์ฝ๋ ๊ฐ์ ธ์ค๊ธฐ
    - git bash์์
    ```
    $ git clone https://lab.ssafy.com/s07-webmobile3-sub2/S07P12A208.git
    ```
- ๋ผ์ฆ๋ฒ ๋ฆฌํ์ด์ ์ฝ๋ ๋ฃ๊ธฐ
    - cloneํ dir์์ HW/VOICE_DETECTION ๋ด์ ์๋ ํ์ผ(version_0 dir ์ ์ธ)๋ฅผ ๋ชจ๋ ๋ผ์ฆ๋ฒ ๋ฆฌํ์ด์ ~/WAVEGO/RPi ๋ด๋ก ์ฎ๊น
### ๐ก๏ธ ๋ชจ๋ ์ธํ
- ์ฌ์ฉํ  ๋ชจ๋
    - OLED 128x64 I2C ์ง์ 2EA 
    - DHT11 ์จ์ต๋ ์ผ์
    - MQ-135 Gas ์ผ์
    - TTP223 ์ ์ ์ ํฐ์น์ผ์
    - HC-SR04 ์ด์ํ ์ผ์
    - 3.5mm ์คํผ์ปค
    - USB ๋ง์ดํฌ 2๊ฐ
- ๋ชจ๋ 3.3V ์ฌ์ฉ
- Pin Map
    | ์ผ์ | ์ผ์ pin | RPI ํ|
    |:--:|:--:|:--:|
    |Touch|Data|GPIO 4|
    |GAS|Data|GPIO 17|
    |DHT11|Data|GPIO 18|
    |์ด์ํ|Data1|GPIO 27|
    |์ด์ํ|Data2|GPIO 22|
    |OLED|SDA|GPIO 2|
    |OLED|SCL|GPIO 3|
    |VCC||board 1|
    |GND||board 14|
    
    - ๋ชจ๋  ์ผ์์ VCC, GND๋ ๋นตํ์ ์ด์ฉํ์ฌ ํ์ ํ๊ธฐ๋ VCC, GND์ ์ฐ๊ฒฐ
    - OLED 2๊ฐ์ SDA, SCL์ ๊ฐ๊ฐ ๋นตํ์ ์ด์ฉํ์ฌ ํ์ ํ๊ธฐ๋ SDA, SCL์ ์ฐ๊ฒฐ(๋์ผํ ์ ํธ๋ฅผ OLED 2๊ฐ์์ ๋ฐ์)
- 3.5mm ์คํผ์ปค๋ 3.5mm ์ญ์ ์ฐ๊ฒฐํ์ฌ ์ฌ์ฉ
- USB ๋ง์ดํฌ 2๊ฐ๋ ๋ผ์ฆ๋ฒ ๋ฆฌํ์ด USB 2.0์ ๊ฐ๊ฐ ๊ฝ์ ์ฌ์ฉ
1. I2C ํต์  ํ์ฑํ
    ```
    $ sudo raspi-config
    ```
    3. Interface Options โ P5. I2C
2. ๋ผ์ด๋ธ๋ฌ๋ฆฌ ์ค์น
    ```
    $ git clone https://github.com/adafruit/Adafruit_Python_SSD1306.git
    $ cd Adafruit_Python_SSD1306
    $ sudo python3 setup.py install
    $ sudo pip3 install Adafruit_BBIO
    $ pip3 install adafruit-circuitpython-dht
    $ sudo apt-get install libgpiod2
    $ python3 -m pip install mysql-connector
    $ python3 -m pip install mysql-connector-python
    ```
3. ์ผ์ ์ฐ๊ฒฐ ํ์คํธ
    ```
    $ python3 ~/WAVEGO/RPi/mysql_sensing.py
    ```

### ๐ข ์์ฑ ์ธ์ ์ธํ
- ๋ผ์ฆ๋ฒ ๋ฆฌํ์ด4B Debian Buster ๋ฒ์ (2022.07.26 ๊ธฐ์ค RPI imager์ legacy ๋ฒ์ )

1. [Google Speech to Text console start guide](https://cloud.google.com/speech-to-text/docs/transcribe-console?hl=ko)๋ฅผ ๋ฐ๋ผ ํ๋ก์ ํธ ์ค์  ์งํ
    - ํ๋ก์ ํธ ์์ฑ
    - `์ฌ์ฉ์ ์ธ์ฆ ์ ๋ณด` ํ์ด์ง ์๋จ `+ ์ฌ์ฉ์ ์ธ์ฆ ์ ๋ณด ๋ง๋ค๊ธฐ-> ์๋น์ค ๊ณ์ -> ๊ณ์  ์ด๋ฆ ์ค์ `
    - ๋ง๋  ์๋น์ค ๊ณ์  ํด๋ฆญ ํ์ด์ง ์๋จ ๋ฉ๋ด ๋ฐ์ `ํค-> json`  ํค ๋ง๋ค๊ธฐ ํ์ฌ json ํค ๋ค์ด ๋ฐ๊ธฐ
    - ๋ผ์ฆ๋ฒ ๋ฆฌํ์ด์ ํด๋น ํค ํ์ผ ์ ์ฅ
2. [python ํ๊ฒฝ ์ธํ](https://cloud.google.com/python/docs/setup)
    
    ```
    sudo apt update
    sudo apt install python3 python3-dev python3-venv
    sudo apt-get install wget
    wget https://bootstrap.pypa.io/get-pip.py
    sudo python3 get-pip.py
    pip3 --version
    
    cd your-project
    python3 -m venv env
    source env/bin/activate
    ```
    

3. google cloud speech ์ค์น

4. client library ์ค์น
    ```
    pip install --upgrade google-cloud-speech
    ```

5. `export GOOGLE_APPLICATION_CREDENTIALS="KEY_PATH"` ๋ฅผ ์ด์ฉํ์ฌ ์ด์ ์ RPI์ ๋ฃ์ด๋์ key ํ์ผ ๋ฑ๋ก
    - ์ด ๋ ์๋ ๊ฒฝ๋ก๋ก ํ๋ฉด ์ฐพ์ ์ ์๋ค๋ ์๋ฌ๊ฐ ๋ฐ์ํ๋ฏ๋ก **์ ๋ ๊ฒฝ๋ก**๋ฅผ ์ฌ์ฉํ  ๊ฒ
6. ๋ผ์ฆ๋ฒ ๋ฆฌํ์ด OS ๋ฒ์  ์ด์ ํด๊ฒฐ
    - `ImportError: /lib/arm-linux-gnueabihf/libm.so.6: version GLIBC_2.29 not found (required by /home/pi/google_stt/env/lib/python3.7/site-packages/grpc/_cython/cygrpc.cpython-37m-arm-linux-gnueabihf.so)` ๋ฐ์
        - Google PubSub๊ฐ Debian GLIBC 2.29๋ฅผ ์ง์ํ์ง ์๋ ๊ฒ์ผ๋ก ๋ณด์
        - ํด๊ฒฐ ๋ฐฉ์์ผ๋ก๋ ์๋ ๋ ๊ฐ์ง ์กด์ฌ
            - ๋ผ์ฆ๋ฒ ๋ฆฌํ์ด์ OS๋ฅผ Ubuntu๋ก ๋ณ๊ฒฝ.
            - PATH๋ฅผ ์ค์ ํ ํ grpcio๋ฅผ ๋ค์ ์ค์น
            
            ํ๋ก์ ํธ ํน์ฑ ์ ๋ผ์ฆ๋ฒ ๋ฆฌํ์ด์ OS๋ฅผ ๋ณ๊ฒฝํ๋ ๊ฒ์ ๋ถ๊ฐ๋ฅ ํ์ผ๋ฏ๋ก ๋ ๋ฒ์งธ ๋ฐฉ๋ฒ ์ฌ์ฉ
            
            1. ํ์คํธ ์๋ํฐ๋ก /home/pi/.bashrc ์ ์๋ ์ค ์ถ๊ฐ
                
                `export PATH="$HOME/.local/bin:$PATH"`
                
            2. ์๋ ๋ช๋ น์ด ์คํ
                
                ```
                pip uninstall grpcio
                pip uninstall grpcio-status
                pip install grpcio==1.44.0 --no-binary=grpcio
                pip install grpcio-tools==1.44.0 --no-binary=grpcio-tools
                ```
                
                3, 4๋ฒ์งธ ๋ช๋ น์ด ํฉ์ณ ์คํํ๋๋ฐ 1์๊ฐ ์ ๋ ๊ฑธ๋ฆผ

7. google stt ์งํํ๋ ๋๋ก /home/pi/google_stt ๋ด ์ค์ ๋ env activate(`source env/bin/activate`)
8. `pvporcupine, pvporcupinedemo` ๊ฐ์ ํ๊ฒฝ ๋ด ์ค์น
    ```
    pip3 install pvporcupine
    pip3 install pvporcupinedemo
    ```
9. ๋ผ์ฆ๋ฒ ๋ฆฌํ์ด์ ํ๋ก์ ํธ ํด๋๋ก ์ด๋
    ```
    $ cd ~/WAVEGO/RPi
    ```
10. ํ์ํ ๋ผ์ฆ๋ฒ ๋ฆฌํ์ด ์ค์น
    ```
    $ (env) pip install -r voice_requirements.txt
    ```
11. ์ฐ๊ฒฐ๋ ๋ง์ดํฌ ํ์ธ
    ```
    $ (env) porcupine_demo_mic --show_audio_devices
    ```
    ๊ฒฐ๊ณผ ์์
    ```
    index: 0, device name: USB PnP Sound Device Analog Mono
    index: 1, device name: USB PnP Sound Device Analog Mono
    index: 2, device name: Monitor of Built-in Audio Analog Stereo
    ```
    - USB ๋ง์ดํฌ๊ฐ 2๊ฐ ์ธ์๋๋ฉด ์ ๋จ
12. ํ์ผ ์คํ(๊ฐ์ ํ๊ฒฝ ์์ด๋ ๋จ)
    - 11๋ฒ๊น์ง๋ ์ด๊ธฐ์๋ง ์งํํ๋ฉด ๋จ
    ```
    $ ~/WAVEGO/RPi/voice.sh [๋ง์ดํฌ index] [user id]
    ```
    - ๋ง์ดํฌ index๋ ์์์ ๋ณด๋ ๊ฒ ์ค USB ๋ง์ดํฌ 0 ์ ์ธ 1 ํน์ 2๋ก ์งํํ๋ฉด ๋จ
    - user id๋ ์น์์ ๋ฐ์ DB์ ์์ด๋

### ๐ MQTT ํต์  ์ธํ
- WEB๊ณผ ์ ํธ๋ฅผ ์ฃผ๊ณ  ๋ฐ๊ธฐ ์ํด MQTT ์ฌ์ฉ
- ๋ผ์ฆ๋ฒ ๋ฆฌํ์ด์ ์ฝ๋ ๋ฃ๊ธฐ
    - cloneํ dir์์ HW/MQTT ๋ด์ ์๋ ํ์ผ(version_0 dir ์ ์ธ)๋ฅผ ๋ชจ๋ ๋ผ์ฆ๋ฒ ๋ฆฌํ์ด์ ~/WAVEGO/RPi ๋ด๋ก ์ฎ๊น
1. google stt ์งํํ๋ ๋๋ก /home/pi/google_stt ๋ด ์ค์ ๋ env activate(`source env/bin/activate`)
2. ํ์ํ ๋ผ์ด๋ธ๋ฌ๋ฆฌ๋ voice_requirements.txt์์ ์ด๋ฏธ ์ค์น ์๋ฃ
3. ์คํ
    ```
    $ ~/WAVEGO/RPi/mqtt.sh [user id]
    ```
4. ํ์คํธ 
    - ๊ฐ์ธ PC์์ clone ๋ฐ์ dir์์ /HW/MQTT/version_0/mqtt_subscribe_test_for_rpi.py๋ฅผ ์ด์ฉํ์ฌ ์ ๋์ํ๋์ง ํ์ธ ๊ฐ๋ฅ
    - ๊ฐ์ธ PC์์
        ```
        $ python mqtt_subscribe_test_for_rpi.py -op1 i7a208.p.ssafy.io
        ```
    - ๋ผ์ฆ๋ฒ ๋ฆฌํ์ด ์ฝ์์์ forward, backward ๋ฑ์ด ์ํ์ด ์ ๋๋ฉด ์ฑ๊ณต

### ๐ฅ Video Streaming
1. ๋ผ์ฆ๋ฒ ๋ฆฌํ์ด์ ๋ผ์ด๋ธ๋ฌ๋ฆฌ ์ค์น
    ```
    $ sudo apt update
    $ sudo apt full-upgrade
    $ sudo apt-get install ffmpeg
    ```
2. ๊ฐ์ธ ๊ตฌ๊ธ ์์ด๋๋ก ์ ํ๋ธ ์ ์
3. ์คํธ๋ฆฌ๋ฐ ์์ํ์ฌ ํค ์ป๊ธฐ
4. ๋ผ์ฆ๋ฒ ๋ฆฌํ์ด์์ cmd ์คํ
    ```
    $ ffmpeg -re -i /dev/video0 -f lavfi -i anullsrc -vb 2500k -s 1280x720 -f flv [youtube streaming ํค]
    ```

### ๐ S3 access key ๋ฑ๋ก
1. AWS์ ๋ก๊ทธ์ธ
2. [IAM console](https://console.aws.amazon.com/iam) ๋ก ์ด๋
3. `My Security Credentials โ Access Keys` ๋ก ์ด๋
4. `Create New Access Key` ๋ก ์๋ก์ด ํค ๋ง๋ค๊ธฐ
5. csv ํ์ผ ๋ค์ด ๋ฐ๊ธฐ
6. ๋ผ์ฆ๋ฒ ๋ฆฌํ์ด์ ์๊ฒฉ์ผ๋ก ์ ์ํด์ ๋ฐ์ ํค ๋ฑ๋ก
    ```
    $ aws configure
    ```
    - ๊ฐ์ธ PC๋ก ๋ฐ์ csv ํ์ผ์ ์ด์ด ์ ํ ์๋ access key, secret key ๋ฑ๋ก
 [AWS key ๋ง๋ค๊ธฐ](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html#Using_CreateAccessKey)
 [key ๋ฑ๋ก](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html)

## ๐ฒ File Structure
```
๐HW
โโDESIGN           // 3D models
|
โโDOCS
โ  โโideas
โ  โ  โโassets
โ  โโtips
โ      โโassets
|
โโGESTURE_SENSOR   // ํฐ์น ์ผ์
โ  โโimg
|  โโtest
|  โโgo_oled.py
|  โโmysql_sensing.py
|  โโoled_touch.py
|  โโsensor pin.txt
|
โโMQTT             // web & robot ํต์ 
โ  โโversion_0
โ  โ  โโmqtt_in_js
โ  โโmqtt.sh
โ  โโmqtt_subscribe.py
โ
โโOBJECT_DETECTION  // ์์ด ํ์ต
โ  โโobject_img
โ  โโtest_img
โ  โโoutput.xml
โ 
โโOPENCV           // ์์ด ์ธ์ & following
โ  โโversion_0
โ  โโcamera_opencv.py
โ  
โโSENSORS           // ์ผ์ ์ธํ
โ  โโtest
โ  โโversion_0
โ  โโ[sensor] setting_audio.md
โ  โโ[sensor] setting_dht11.md
โ  โโ[sensor] setting_gas.md
โ  โโ[sensor] setting_oled.md
โ  โโ[sensor] setting_sonic.md
โ  โโ[sensor] setting_touch.md
โ  โโsensor_requirements.txt
|
โโSTREAMING        // YouTube streaming
โโVOICE_DETECTION  // ์์ฑ ์ธ์
โ  โโimg           // OLED์ ์ฌ์ฉ๋๋ ํ์ 
โ  โโversion_0
โ  โ  โโGoogle_STT
โ  โ  โ  โโresources
โ  โ  โ  โโresults
โ  โ  โโPICOVOICE
โ  โ  โโVOICE_DETECTION
โ  โ  โโVOICE_MSSG
โ  โโvoice_data    // story, key, ํ๊ธ ๋ชจ๋ธ
โ  โโsensor pin.txt
โ  โโsensor_mysql.py
โ  โโsensor_oled.py
โ  โโsensor_touch.py
โ  โโvoice.py
โ  โโvoice.sh
โ  โโvoice_porcupine_custom.py
โ  โโvoice_recognition.py
โ  โโvoice_requirements.txt
โ  โโvoice_s3_mssg.py
โ  โโvoice_speaker.py
|
โโWAVEGO           // WAVEGO code 
   โโDemo_code
   โ  โโWAVEGO_Demo_Code_(Arduino)_220128.zip
   โ  โโWAVEGO_Demo_Code_(Pi)_220128.zip
   โโversion_0
   โ  โโ์ฝ๋ ์์  ํ ์ ์ฉ.md
   โ  โโ์ผ๊ตด ํ์ต ์ฌ์ฉ๋ฒ ์ ๋ฆฌ.md
   โ  โโWebPage_0811.h
   โ  โโWAVEGO_0811.ino
   โ  โโServoCtrl_0811.h
   โ  โโrobot_0811.py
   โ  โโcamera_opencv_0810.py
   โ  โโ[WAVEGO] 0803_code_modify.md
   โ  โโ[WAVEGO] 0804_code_modify.md
   โ  โโ[WAVEGO] 0809_code_modify.md
   โ  โโ[WAVEGO] 0811_code_modify.md
   โ  โโ[WAVEGO] code_analysis.md
   โโ[WAVEGO] demo_code_flow.md
   โโrobot.py

 ```
+ version_0: ๊ฐ๋ฐ ์ค์ ์์ฑํ ํ์ผ๋ค
## ๐ ์ฐจํ ๋ณด์์ 
- ๋ชจ๋ธ๋ง ๋ ๊ท์ฝ๊ฒ ๊ฐ์ 
- ํฐ์น ์ผ์ ์ฌ๋ฌ ๊ณณ์ ๋ถ์ฐฉ
- ROS ์ด์ฉ ์ด๋ค ๋ฐฉ์ธ์ง ์ธ์
- OLED ๊ฐ๊ฐ ๋ค๋ฅธ ํ์  ํ์
- ์ผ๊ตด์ ๋ชจํฐ๋ฅผ ๋ฌ์ ๊ณ ๊ฐ ๋๋์ด๊ธฐ ๋ถ๋๋ฝ๊ฒ ์งํ
- Google STT ๋์  ๋ก์ปฌ์์ ๋์๊ฐ๋ STT ์ด์ฉ delay ์ค์ด๊ธฐ
- ๋ง์ดํฌ 1๊ฐ ์ฌ์ฉํ๋ฉด์ ์์ฑ ์ธ์ ์งํ
- ๊ฐ๋ ๋์ ๋ง์ดํฌ ์ฌ์ฉ
- ์ฐํ๊ฐ ํ์ฌ๋ ์คํผ์ปค ์ฌ์ฉ
- ์์ด์ ๋ํํ๋ ๊ธฐ๋ฅ
- ๋ผ์ฆ๋ฒ ๋ฆฌํ์ด CPU ์จ๋ ์ฟจ๋ง