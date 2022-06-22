from Deepracer import deepracer
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

    for i in range(1, 3):
        dr.set_led_color(0,0,0,rand=True)
        time.sleep(.2)

    print(dr.get_battery_level())

    sensor_status = dr.get_sensor_status()
    print(sensor_status)

    drive_status = dr.set_drive_mode_to_manual()
    print(drive_status)
    start_status = dr.start()
    print(start_status)
    let_us_drive = dr.manual_drive_forward(0, 1, 1)
    time.sleep(3)
    print(let_us_drive)
    let_us_drive = dr.manual_drive_reverse(0, 1, 1)
    time.sleep(3)
    print(let_us_drive)
    dr.stop()
else:
    print("Login Failed ...")



