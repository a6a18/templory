import requests
import json


def login():
    url = "https://twproxy01.svc.litv.tv//cdi/v2/rpc"

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
                "text": "it 邦幫忙鐵人賽"
            }
        ]
    }

    requests.post(url=url, headers=headers, data=json.dumps(data))


if __name__ == '__main__':
    send_message()
