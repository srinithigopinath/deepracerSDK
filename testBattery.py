from Deepracer import deepracer as deepracer
import random
import time

dr = deepracer.Deepracer(base_url='https://192.168.1.147', password='Merck12+0$')

if dr.login():
    print('Login Successful ...')
    print(dr.get_battery_level())
    dr.stop()
else:
    print("Login Failed ...")



