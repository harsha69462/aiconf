import random

def ldr_input():
    device_id = "0002B"
    type = "light sensor"
    ldr_inp = random.randint(0,1)
    return [device_id,type,ldr_inp]