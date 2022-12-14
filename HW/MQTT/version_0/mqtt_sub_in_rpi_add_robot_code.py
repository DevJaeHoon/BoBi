import paho.mqtt.client as mqtt
import robot_test
from s3_voice_mssg import VoiceMessage
import argparse

_mqtt_broker_ip = "[server ip]"

speedMove = 100


def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # subscribe on predefined topics for robot_test
    client.subscribe(_user_id + "/move/forward")
    client.subscribe(_user_id + "/move/backward")
    client.subscribe(_user_id + "/move/left")
    client.subscribe(_user_id + "/move/right")
    client.subscribe(_user_id + "/voice/torobot")
    client.subscribe(_user_id + "/gesture")


def on_forward(client, userdata, msg):
    global speedMove
    print("forward " + str(msg.payload))
    if msg.payload == "on":
        robot_test.forward(speedMove)
    elif msg.payload == "off":
        robot_test.stopFB()


def on_backward(client, userdata, msg):
    global speeedMove
    print("backward " + str(msg.payload))
    if msg.payload == "on":
        robot_test.backward(speedMove)
    elif msg.payload == "off":
        robot_test.stopFB()


def on_left(client, userdata, msg):
    global speedMove
    print("left " + str(msg.payload))
    if msg.payload == "on":
        robot_test.left(speedMove)
    elif msg.payload == "off":
        robot_test.stopLR()


def on_right(client, userdata, msg):
    global speedMove
    print("right " + str(msg.payload))
    if msg.payload == "on":
        robot_test.right(speedMove)
    elif msg.payload == "off":
        robot_test.stopLR()


def on_torobot(client, userdata, msg):
    print("torobot_test " + str(msg.payload))
    mssg_file_name = _user_id + "_from_web.wav"
    voice_mssg = VoiceMessage()
    voice_mssg.download_file(mssg_file_name)


def on_powersaving_on(client, userdata, msg):
    print("power saving on " + str(msg.payload))


def on_powersaving_off(client, userdata, msg):
    print("power saving off " + str(msg.payload))


def on_gesture(client, userdata, msg):
    print("gesture " + str(msg.payload))
    if msg.payload == "handshake":
        robot_test.handShake()
    elif msg.payload == "steady":
        robot_test.steadyMode()
    elif msg.payload == "jump":
        robot_test.jump()
    elif msg.payload == "sit":
        robot_test.sit()
    elif msg.payload == "standUp":
        robot_test.standUp()
    elif msg.payload == "leftHand":
        robot_test.leftHand()
    elif msg.payload == "rightHand":
        robot_test.rightHand()
    elif msg.payload == "lower":
        robot_test.lower()
    elif msg.payload == "upper":
        robot_test.upper()


parser = argparse.ArgumentParser()
parser.add_argument('--user_id',
                    help="User ID registered in DB in integer")
args = parser.parse_args()
_user_id = args.user_id

client = mqtt.Client()
client.on_connect = on_connect
client.message_callback_add(_user_id + "/move/forward", on_forward)
client.message_callback_add(_user_id + "/move/backward", on_backward)
client.message_callback_add(_user_id + "/move/left", on_left)
client.message_callback_add(_user_id + "/move/right", on_right)
client.message_callback_add(_user_id + "/voice/torobot", on_torobot)
client.message_callback_add(_user_id + "/gesture", on_gesture)

# connect to broker
client.connect(_mqtt_broker_ip, 1883, 60)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()
