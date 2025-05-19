from flask import Flask, request

app = Flask(__name__)

@app.route('/_api_/', methods=['POST'])
def log_behavior():
    d = request.get_json()
    ip = request.headers.get('X-Forwarded-For', request.remote_addr)

    print("\n>> Registro de actividad detectado:")
    print(f"IP: {ip}")
    print(f"U: {d.get('u')}")
    print(f"C: {d.get('c')}")
    print(f"T: {d.get('t')}")
    print(f"TT (tiempo total): {d.get('tt')} ms")
    print(f"B (backspaces): {d.get('b')}")
    print(f"VC (cambios de visibilidad): {d.get('vc')}")
    print(f"PC (¿pegado?): {'Sí' if d.get('pc') else 'No'}")
    print(f"KD (key delays): {d.get('kd')}\n")

    return '', 204

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5050)
