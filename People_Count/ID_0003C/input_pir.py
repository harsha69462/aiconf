import random


def pir_input():
    device_id = "0003C"
    type = "people count sensor"
    people_count=random.randint(0, 5)
    return [device_id,type, people_count]