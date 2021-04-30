#######################################################################################################################
# NAME: Antoine AUger-Maroun, Carl Genest
# TIME:23/04/2021
#FILE: hue.py
# OBJECT: Retrives info from connected light and send it to API team
#######################################################################################################################


from cloudMQTT import *
from phue import Bridge
import json
import time
from datetime import datetime


b = None
mqtt = None


def init():
    global b
    global mqtt

    b = Bridge('192.168.0.127')
    b.connect()
    b.get_api()

    mqtt = connectionMQTT(
        'mqtt://ghhtzpps:MwVNHJbYYirC@driver-01.cloudmqtt.com:18760', '/C64/Projet/Equipe1/Capteur')


def lightStatus():
    light = b.lights
    lights = {}
    for l in light:
        lights[len(lights)] = (b.get_light(l.name))

    status = {}
    for index in lights:
        print(lights[index])
        status[len(status)] = {"id": lights[index]['uniqueid'],
                               "date": datetime.now().isoformat(),
                               "type": "light",
                               "valeur": lights[index]['state']['on'],
                               "alerte": 0,
                               "messageAlerte": None}

    print(status)
    return status


def openLights():
    light = b.lights
    for l in light:
        b.set_light(l.name, 'on', True)


def closeLights():
    light = b.lights
    for l in light:
        b.set_light(l.name, 'off', True)


def loop():

    INTERVAL = 300.0

    while True:

        currentTime = time.time()

        time.sleep(INTERVAL - currentTime % INTERVAL)

        mqtt.publish(lightStatus(), str(dt.datetime.now()))

        currentTime = time.localtime(currentTime)

        if currentTime.tm_hour == 20:
            openLights()

        elif currentTime.tm_hour == 8:
            closeLights()


def main():

    init()
    loop()
    


if __name__ == '__main__':
    main()
