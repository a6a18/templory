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


if __name__ == '__main__':
    login()
