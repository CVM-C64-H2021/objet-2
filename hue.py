#######################################################################################################################
# NAME: Antoine AUger-Maroun, Carl Genest
#TIME:23/04/2021
#FILE: hue.py
#OBJECT: Retrives info from connected light and send it to API team
#######################################################################################################################


from cloudMQTT import *
from phue import Bridge
import json
import time
import datetime as dt



def lightStatus():
    light = b.lights
    lights = {}
    for l in light:
        lights[len(lights)] = (b.get_light(l.name))


    status = {}
    for index in lights:
        status[len(status)] = {"name":lights[index]['name'],"on":lights[index]['state']['on']}

    return status




b = Bridge('192.168.0.127')

b.connect()

b.get_api()

mqtt = connectionMQTT('mqtt://ghhtzpps:MwVNHJbYYirC@driver-01.cloudmqtt.com:18760', '/C64/Projet/Equipe1/Capteur')

status= lightStatus()


oldTime = time.localtime(time.time())
alreadySend = False
while True:
    
    newTime = time.localtime(time.time())

    if newTime.tm_hour != oldTime.tm_hour:
        alreadySend = False
    

    if newTime.tm_hour == 8 and newTime.tm_min == 0 and not alreadySend:
        alreadySend = True
        status=lightStatus()
        mqtt.publish(status, str(dt.datetime.now()))
        print(status)
        oldTime = newTime

    



