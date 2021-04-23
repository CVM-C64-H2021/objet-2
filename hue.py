from phue import Bridge
import json
import time



def lightStatus():
    light = b.lights
    lights = {}
    for l in light:
        lights[len(lights)] = (b.get_light(l.name))


    status = {}
    for index in lights:
        print(f"{lights[index]['state']['on']} ------ {lights[index]['name']}")
        status[len(status)] = {"name":lights[index]['name'],"on":lights[index]['state']['on']}

    return status




b = Bridge('192.168.0.127')

b.connect()

b.get_api()




status= lightStatus()
print(status)


# while True:
#     localtime = time.localtime(time.time())

#     if(localtime.tm_hour == 8 & & localtime.tm_min == 0){
#         # TODO: Send light status
#         status=lightStatus()
#         print(status)
#     }



