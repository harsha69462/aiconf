from Temperature.ID_0001A.dht11 import *
from Temperature.ID_0001B.dht11 import *
from Light.ID_0002B.ldr import *
from People_Count.ID_0003C.pir import *
from queue import Queue
import json

op_queue = Queue(10)

class Output(Thread):
    def run(self):
        while True:
            time.sleep(2)
            Dht_Sensor_one_Start()
            Dht_sensor_two_Start()
            Ldr_sensor_one_Start()
            Pir_sensor_one_Start()
            global op_queue
            op_queue.put((
                 Dht_sensor_one_Consumer().return_status(),
                 Dht_sensor_two_Consumer().return_status(),
                 Ldr_sensor_one_Consumer().return_status(),
                 Pir_sensor_one_Consumer().return_status()
            ))


class OutputConsumer(Thread):
    def run(self):
        global op_queue
        while True:
            time.sleep(2.2)
            output_data = op_queue.get()
            op_queue.task_done()
            # print(output_data)
            output_json = json.dumps(output_data, indent=4)
            print(output_json)


Output().start()
OutputConsumer().start()