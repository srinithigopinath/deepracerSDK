import json
from requests_html import HTMLSession
from urllib3.exceptions import InsecureRequestWarning
import urllib3

urllib3.disable_warnings(InsecureRequestWarning)


class Deepracer:
    def __init__(self, base_url: str, password: str):
        self.__password = password
        self.__base_url = base_url
        self.__login_url = f'{base_url}/login'
        self.__set_led_color_url = f'{base_url}/api/set_led_color'
        self.__get_led_color_url = f'{base_url}/api/get_led_color'
        self.__get_battery_level_url = f'{base_url}/api/get_battery_level'
        self.__start_stop_url = f'{base_url}/api/start_stop'
        self.__set_calibration_mode_url = f'{base_url}/api/set_calibration_mode'
        self.__get_sensor_state_url = f'{base_url}/api/get_sensor_status'
        self.__drive_mode_url = f'{base_url}/api/drive_mode'
        self.__manual_drive_url = f'{base_url}/api/manual_drive'
        self.__mjpeg_stream_url = f'{base_url}/route?topic=/camera_pkg/display_mjpeg'
        self.__cookies = None
        self.__session_token = None

    def __get_csrf_token(self):
        self.__session = HTMLSession()
        self.__session.verify = False
        r = self.__session.get(self.__login_url)
        meta_tags = r.html.find('meta')
        self.__cookies = r.cookies
        self.__csrf_tokens = [meta.attrs['content'] for meta in meta_tags if meta.attrs['name'] == 'csrf-token']

    def login(self):
        self.__get_csrf_token()

        if len(self.__csrf_tokens) <= 0 or len(self.__cookies) <= 0:
            raise Exception("Unable to obtain csrf-token or session cookie")
        self.__session_token = self.__cookies.get_dict()['session']
        data = dict()
        headers = dict()
        data['password'] = self.__password
        headers['Content-Type'] = 'application/x-www-form-urlencoded'
        headers['Cookie'] = f'session={self.__session_token}'
        headers['X-CSRFToken'] = self.__csrf_tokens[0]
        response = self.__session.post(self.__login_url, headers=headers, data=data, verify=False)

        if response.status_code != 200:
            print(f'Unable to login {response.text}')
            return False
        self.__cookies = response.cookies
        return True

    def __make_header(self):
        headers = dict()
        headers['Content-Type'] = 'application/json'
        headers['X-CSRF-Token'] = self.__csrf_tokens[0]
        headers[
            'Cookie'] = f'session={self.__session_token}; deepracer_token={self.__cookies.get_dict()["deepracer_token"]}'
        return headers

    def __set_lead_color(self, r, g, b):
        data = {"red": r, "green": g, "blue": b}
        response = self.__session.post(self.__set_led_color_url, headers=self.__make_header(), json=data,
                                       cookies=self.__cookies,
                                       verify=False)
        if response.status_code != 200:
            print(f'Unable to set the LED COLOR {response.text}')
            return False
        return True

    def set_led_color(self, r, g, b, rand=False):
        if rand:
            return self.__set_lead_color(random.randint(100, 255), random.randint(100, 255), random.randint(100, 255))
        else:
            return self.__set_lead_color(r, g, b)

    def get_led_color(self):
        response = self.__session.get(self.__get_led_color_url, headers=self.__make_header(), cookies=self.__cookies,
                                      verify=False)
        if response.status_code != 200:
            print(f'Unable to get the LED COLOR {response.text}')
            return json.dumps(response)
        return json.loads(response.text)

    def get_battery_level(self):
        response = self.__session.get(self.__get_battery_level_url, headers=self.__make_header(),
                                      cookies=self.__cookies,
                                      verify=False)
        if response.status_code != 200:
            print(f'Unable to get the LED COLOR {response.text}')
            return json.dumps(response)
        return json.loads(response.text)

    def stop(self):
        data = {"start_stop": "stop"}
        response = self.__session.put(self.__start_stop_url, headers=self.__make_header(), json=data,
                                      cookies=self.__cookies,
                                      verify=False)
        if response.status_code != 200:
            print(f'Unable to STOP VehicleR {response.text}')
            return json.dumps(response)
        return json.loads(response.text)

    def start(self):
        data = {"start_stop": "start"}
        response = self.__session.put(self.__start_stop_url, headers=self.__make_header(), json=data,
                                      cookies=self.__cookies,
                                      verify=False)
        if response.status_code != 200:
            print(f'Unable to STOP VehicleR {response.text}')
            return json.dumps(response)
        return json.loads(response.text)

    def set_drive_mode_to_manual(self):
        data = {"drive_mode": "manual"}
        response = self.__session.put(self.__drive_mode_url, headers=self.__make_header(), json=data,
                                      cookies=self.__cookies,
                                      verify=False)
        if response.status_code != 200:
            print(f'Unable to STOP VehicleR {response.text}')
            return json.dumps(response)
        return json.loads(response.text)

    def set_drive_mode_to_auto(self):
        data = {"drive_mode": "auto"}
        response = self.__session.put(self.__drive_mode_url, headers=self.__make_header(), json=data,
                                      cookies=self.__cookies,
                                      verify=False)
        if response.status_code != 200:
            print(f'Unable to STOP VehicleR {response.text}')
            return json.dumps(response)
        return json.loads(response.text)

    def set_calibration_mode(self):
        response = self.__session.get(self.__set_calibration_mode_url, headers=self.__make_header(),
                                      cookies=self.__cookies,
                                      verify=False)
        if response.status_code != 200:
            print(f'Unable to get the LED COLOR {response.text}')
            return json.dumps(response)
        return json.loads(response.text)

    def get_sensor_status(self):
        response = self.__session.get(self.__get_sensor_state_url, headers=self.__make_header(),
                                      cookies=self.__cookies,
                                      verify=False)
        if response.status_code != 200:
            print(f'Unable to get the LED COLOR {response.text}')
            return json.dumps(response)
        return json.loads(response.text)

    def manual_drive(self, angle, max_speed, throttle):
        data = {"angle": angle, "max_speed": max_speed, "throttle": throttle}
        response = self.__session.put(self.__manual_drive_url, headers=self.__make_header(), json=data,
                                      cookies=self.__cookies,
                                      verify=False)
        if response.status_code != 200:
            print(f'Unable to STOP VehicleR {response.text}')
            return json.dumps(response)
        return json.loads(response.text)

    def get_mjpeg_stream_url(self, width=480, height=360):
        return f'{self.__mjpeg_stream_url}&width={width}&height={height}'

    # def get_camera_image(self, width=480, height=360):
    #     ssl_context = ssl.create_default_context()
    #     ssl_context.check_hostname = False
    #     ssl_context.verify_mode = ssl.CERT_NONE
    #     request = Request(self.get_mjpeg_stream_url(width, height))
    #     headers = self.__make_header()
    #     for name in headers:
    #         request.add_header(name, headers[name])
    #     stream = urlopen(request, context=ssl_context)
    #     _bytes = bytes()
    #     while True:
    #         _bytes += stream.read(1024)
    #         a = _bytes.find(b'\xff\xd8')
    #         b = _bytes.find(b'\xff\xd9')
    #         if a != -1 and b != -1:
    #             jpg = _bytes[a:b + 2]
    #             _bytes = _bytes[b + 2:]
    #             img = cv2.imdecode(np.fromstring(jpg, dtype=np.uint8), cv2.IMREAD_COLOR)
    #             break
    #     return img
