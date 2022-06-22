from Deepracer import deepracer as deepracer
import random
import time

dr = deepracer.Deepracer(base_url='https://192.168.1.147', password='Merck12+0$')

if dr.login():
    print('Login Successful ...')
    sensor_status = dr.get_sensor_status()
    print(sensor_status)
    dr.stop()
else:
    print("Login Failed ...")



