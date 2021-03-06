import requests
import json
import time
import logging
import os
import random


FORMAT = '%(asctime)s %(levelname)s: %(message)s'

logging.basicConfig(level=logging.INFO,
                    filename='login.log',
                    format=FORMAT)


def send_message():
    url = 'https://api.line.me/v2/bot/message/push'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer d9vni23HMrx9az1UDeIfbJakTOAaVTslK4tqNyWxSRgmj6zTaswif5tegG2tvqOnCBtxnSPKe6nRfXe4M17s7olhVeP32AThNIR+T616SLS771J9irXZhgUduz3sr83rNOGg7QcpH0hFogGJyOExhgdB04t89/1O/w1cDnyilFU='
    }
    data = {
        "to": "Uf1df2ac474299d93846191f0135f95df",
        "messages": [
            {
                "type": "text",
                "text": "login_api有問題唷!"
            }
        ]
    }

    requests.post(url=url, headers=headers, data=json.dumps(data))


def login(proxy_n):
    url = "https://twproxy0{}.svc.litv.tv//cdi/v2/rpc".format(proxy_n)

    data = {
        "jsonrpc": "2.0",
        "id": 26,
        "method": "AccountService.Login",
        "params": {
            "User": "0999999961",
            "Pass": "11111111",
            "DeviceId": "F895C7F2F5AD",
            "Swver": "LTAGP0099999LEP20141118170548",
            "ModelInfo": "lge|LG-H815|p1|p1",
            "project_num": "LTIOS03"
        }
    }
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.post(url=url, headers=headers, data=json.dumps(data), timeout=10)

    if response.status_code != 200 or "result" not in response.json():
        return False
    else:
        return True


if __name__ == '__main__':

    count = 0
    start_time = time.time()
    while True:
        try:
            n = random.randint(1, 6)
            now_time = time.time()
            result = login(n)

            if (now_time - start_time) > 300:  # 5分鐘
                count = 0

            if result == False:
                logging.warning('twproxy{} warning message'.format(n))
                count += 1

            if count >= 2:
                logging.warning('twproxy{} warning message'.format(n))
                send_message()

            time.sleep(30)
        except:
            pass
