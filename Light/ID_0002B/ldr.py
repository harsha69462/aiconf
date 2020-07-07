from threading import Thread
import time
from Light.ID_0002B.input_ldr import *
from queue import Queue
#import requests


ldr_queue = Queue(10)


class Ldr(Thread):
    def run(self):
        while True:
            time.sleep(2)
            device_id, type, ldr_res = ldr_input() #receive sensor data here
            global ldr_queue
            ldr_queue.put({"device_id":device_id,"type": type,"on-off": ldr_res})
            # print("Produced", [cur_temp, cur_humid])

ldr_res = ""


class Ldr_sensor_one_Consumer(Thread):

    def run(self):
        global ldr_queue
        while True:
            time.sleep(2.2)
            global ldr_res
            ldr_res = ldr_queue.get()
            ldr_queue.task_done()
            # print(self.ldr_res)

    def return_status(self):
        return ldr_res



class Ldr_sensor_one_Start():
    def __init__(self):
        Ldr().start()
        Ldr_sensor_one_Consumer().start()


