import os
from flask import Flask, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)  # فعال‌سازی CORS

@app.route('/proxy/nobitex', methods=['GET'])
def nobitex_proxy():
    api_key = os.getenv("API_KEY")  # دریافت کلید API از متغیر محیطی
    headers = {
        "Authorization": f"Token {api_key}"
    }
    response = requests.get("https://api.nobitex.ir/users/wallets/list", headers=headers)
    return jsonify(response.json())

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))  # استفاده از پورت تعیین‌شده توسط Render
    app.run(host="0.0.0.0", port=port)  # تنظیم سرور برای گوش دادن به آدرس عمومی
