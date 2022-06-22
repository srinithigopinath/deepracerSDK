from Deepracer import deepracer as deepracer
import random
import time

dr = deepracer.Deepracer(base_url='https://192.168.1.147', password='Merck12+0$')

if dr.login():
    print('Login Successful ...')
    dr.stop()
    dr.set_calibration_mode()
    time.sleep(1)
    dr.set_led_color(255, 0, 0)
    time.sleep(2)
    colors = dr.get_led_color()
    print(colors)
    dr.set_led_color(0, 255, 0)
    time.sleep(2)
    colors = dr.get_led_color()
    print(colors)
    dr.set_led_color(0, 0, 255)
    time.sleep(2)
    colors = dr.get_led_color()
    print(colors)
    dr.stop()
else:
    print("Login Failed ...")



