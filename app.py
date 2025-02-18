from flask import Flask, render_template, request
from scanner import scan_network
from ai_helper import explain_vulnerability

app = Flask(__name__)

@app.route('/')
def index():
    """Carrega a página principal."""
    return render_template('index.html')

@app.route('/scan', methods=['POST'])
def scan():
    """Recebe um IP e retorna a varredura de portas + explicação da IA."""
    target = request.form.get("target", "192.168.1.1")
    results = scan_network(target)

    for host, ports in results.items():
        for port, info in ports.items():
            service = info.get("name", "desconhecido")
            results[host][port]["ai_explanation"] = explain_vulnerability(port, service)

    return render_template('index.html', results=results)

if __name__ == '__main__':
    app.run(debug=True)
