import json
import os
import os.path
import urllib.parse

import paho.mqtt.client as mqtt


class connectionMQTT():

    def __init__(self, url, topic):
        self.mqttc = mqtt.Client()

        # Parse CLOUDMQTT_URL (or fallback to localhost)
        self.url_str = os.environ.get('CLOUDMQTT_URL', url)
        self.url = urllib.parse.urlparse(self.url_str)
        self.topic = self.url.path[1:] or topic

        self.connection()

    def connection(self):
        # Connect
        self.mqttc.username_pw_set(self.url.username, self.url.password)
        self.mqttc.connect(self.url.hostname, self.url.port)

        # Start subscribe, with QoS level 0
        self.mqttc.subscribe(self.topic, 0)
        # self.mqttc.on_message = self.on_message

        # Continue the network loop, exit when an error occurs
        # rc = 0
        # while rc == 0:
        #     rc = self.mqttc.loop()

    def publish(self, message, date):
        # Publish a message

        res = json.dumps({"value": message})

        self.mqttc.publish(self.topic, res)

    # def on_message(self, client, obj, msg):
    #     message = json.dumps(msg.payload.decode("utf-8"))
    #     print(type(json.loads(message)))  # string?



