from threading import Thread
import time
from Temperature.ID_0001B.input_dht11 import *
from queue import Queue
#import requests

# dht 11 related data
dht_queue = Queue(10)


class Dht11(Thread):
    def run(self):
        while True:
            time.sleep(2)
            device_id, type, cur_temp, cur_humid = dht_input() #receive sensor data here

            global dht_queue
            dht_queue.put({"device_id": device_id, "type": type, "temperature": cur_temp, "humidity": cur_humid})
            # print("Produced", [cur_temp, cur_humid])


dht11_res = ""


class Dht_sensor_two_Consumer(Thread):
    def run(self):
        global dht_queue
        while True:
            time.sleep(2.2)
            global dht11_res
            dht11_res = dht_queue.get()
            dht_queue.task_done()
            # print(dht11_res)

    def return_status(self):
        return dht11_res


class Dht_sensor_two_Start():
    def __init__(self):
        Dht11().start()
        Dht_sensor_two_Consumer().start()


#send sensor data
# dht data end