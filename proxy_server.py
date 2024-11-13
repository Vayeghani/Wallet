from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/proxy/nobitex', methods=['GET'])
def nobitex_proxy():
    # کلید API شما برای نوبیتکس
    api_key = "1fe354df59f01003c967a0023ad55053447e35cd"  # جایگزینی با کلید API واقعی شما
    headers = {
        "Authorization": f"Token {api_key}"
    }
    
    # ارسال درخواست به API نوبیتکس
    response = requests.get("https://api.nobitex.ir/users/wallets/list", headers=headers)
    
    # بازگرداندن پاسخ به صورت JSON
    return jsonify(response.json())

if __name__ == '__main__':
    # اجرای سرور روی پورت 5000
    app.run(port=5000)
