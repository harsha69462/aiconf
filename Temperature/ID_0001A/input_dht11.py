import random

def dht_input():
    #replace sensor code here
        device_id = "0001A"
        type = "temperature sensor"
        cur_temp = 97.5
        cur_humid = 66.0
        op = random.randint(0, 2)
        if op == 1:
            cur_temp += 0.25
            cur_humid += 0.25
        else:
            cur_temp -= 0.25
            cur_humid -= 0.25
        # temp_c = (9/5) * (cur_temp - 32)
        # temp_k = (cur_temp − 32) * (5/9) + 273.15
        return [device_id,type,cur_temp, cur_humid]



