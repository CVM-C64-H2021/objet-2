#######################################################################################################################
# NAME: Antoine AUger-Maroun, Carl Genest
# TIME:23/04/2021
# FILE: hue.py
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

    currentTime = time.localtime()
    light = b.lights
    lights = {}
    for l in light:
        lights[len(lights)] = (b.get_light(l.name))

    for index in lights:

        alerte = 0
        messageAlerte = ""

        if lights[index]['state']['on'] and currentTime.tm_hour < 8 or currentTime.tm_hour > 20:
            alerte = 1
            messageAlerte = "La lumière est fermée alors qu'elle devrait être allumée"

        data = {"idApp": index,
                "date": datetime.now().isoformat(),
                "type": "light",
                "valeur": str(lights[index]['state']['on']),
                "alerte": alerte,
                "messageAlerte": messageAlerte}

        mqtt.publish(data, str(datetime.now()))
    return status


def openLights():
    light = b.lights
    for l in light:
        b.set_light(l.name, 'on', True)


def closeLights():
    light = b.lights
    for l in light:
        b.set_light(l.name, 'on', False)


def loop():

    INTERVAL = 300.0

    while True:

        currentTime = time.time()

        time.sleep(INTERVAL - currentTime % INTERVAL)

        currentTime = time.localtime(currentTime)

        lightStatus()

        if currentTime.tm_hour == 20:
            openLights()

        elif currentTime.tm_hour == 8:
            closeLights()


def main():

    init()
    loop()



if __name__ == '__main__':
    main()
