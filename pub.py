import paho.mqtt.client as mqtt 
import time
from random import uniform

client = mqtt.Client("Coords")  
client.connect("127.0.0.1", 1883, 60)  
client.loop_start()
a = 0
b = 1
while True:
    if a == 10:
        b = -1
    elif a == -1:
        b = 1
    a = a + b

    client.publish("sensors/coords", a)
    print(a, flush=True)
    time.sleep(4)