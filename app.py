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
import string


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



if __name__ == "__main__":
    app.run("0.0.0.0", 5000, debug=True)
