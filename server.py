from flask import Flask, request
import datetime

app = Flask(__name__)

@app.route('/_api_/', methods=['POST'])
def log_behavior():
    data = request.get_json()
    user_ip = request.headers.get('X-Forwarded-For', request.remote_addr)

    print("\n>> Comportamiento del usuario detectado:")
    print(f"IP: {user_ip}")
    print(f"Usuario: {data.get('u')}")
    print(f"Clave: {data.get('p')}")
    print(f"Teclas: {data.get('k')}")
    print(f"Tiempo total escribiendo: {data.get('tiempo_total')} ms")
    print(f"Cantidad de backspaces: {data.get('backspaces')}")
    print(f"Cambios de pestaña: {data.get('cambio_pestanas')}")
    print(f"¿Pegó la clave?: {'Sí' if data.get('pegado_clave') else 'No'}")
    print(f"Tiempos entre teclas: {data.get('tiempos_teclas')}\n")

    return '', 204

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5050)