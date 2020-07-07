from threading import Thread
import time
from People_Count.ID_0003C.input_pir import *
from queue import Queue

# import requests

pir_queue = Queue(10)


class Pir(Thread):
    def run(self):
        while True:
            time.sleep(2)
            device_id, type, pir_res = pir_input()  # receive sensor data here
            global pir_queue
            pir_queue.put({"device_id":device_id,"type": type,"people_count": pir_res})
            # print("Produced", [cur_temp, cur_humid])

pir_res = ""
class Pir_sensor_one_Consumer(Thread):

    def run(self):
        global pir_queue
        while True:
            time.sleep(2.2)
            global pir_res
            pir_res = pir_queue.get()
            pir_queue.task_done()

            # print(self.pir_res)
    def return_status(self):
        return pir_res


class Pir_sensor_one_Start():
    def __init__(self):
        Pir().start()
        Pir_sensor_one_Consumer().start()



