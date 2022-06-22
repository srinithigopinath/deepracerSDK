from Deepracer import deepracer as deepracer
import random
import time

dr = deepracer.Deepracer(base_url='https://192.168.1.147', password='Merck12+0$')

if dr.login():
    print('Login Successful ...')
    drive_status = dr.set_drive_mode_to_manual()
    print(drive_status)
    start_status = dr.start()
    print(start_status)
    let_us_drive = dr.manual_drive(0, 1, -1)
    time.sleep(5)
    dr.stop()
else:
    print("Login Failed ...")



