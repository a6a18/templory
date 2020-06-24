import requests
import re
from flask import Flask, request, abort
from time import sleep
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *
import os
import json


count = os.getenv('count')

app = Flask(__name__)

# Channel Access Token
line_bot_api = LineBotApi(
    'd9vni23HMrx9az1UDeIfbJakTOAaVTslK4tqNyWxSRgmj6zTaswif5tegG2tvqOnCBtxnSPKe6nRfXe4M17s7olhVeP32AThNIR+T616SLS771J9irXZhgUduz3sr83rNOGg7QcpH0hFogGJyOExhgdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('2f853d54aa4d83fe5c408b7cab17b9be')
header = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36',
    'Content-Type': 'application/json'
}


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


# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['GET', 'POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    print("event.reply_token:", event.reply_token)
    print("event.message.text:", event.message.text)

    if "查看數字" in event.message.text:
        
        content = count

        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=content))
        return 0

    if "推送" in event.message.text:
        send_message()


if __name__ == "__main__":
    app.run("0.0.0.0", 5000, debug=True)
