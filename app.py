import os
import subprocess
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return jsonify({"mensagem": "API do osintXHunter online!"})

@app.route("/coleta", methods=["POST"])
def coleta():
    dominio = request.json.get("dominio")
    if not dominio:
        return jsonify({"error": "Domínio não fornecido"}), 400

    executor_script = os.path.abspath("./executor.py")

    comando = [
        "python", executor_script,
        "-d", dominio,
        "-b", "bing"
    ]

    try:
        resultado = subprocess.run(
            comando,
            capture_output=True,
            text=True,
            check=True,
            cwd=os.getcwd()
        )
        return jsonify({"stdout": resultado.stdout})
    except subprocess.CalledProcessError as e:
        return jsonify({
            "error": "Erro ao executar o theHarvester",
            "stdout": e.stdout,
            "stderr": e.stderr
        }), 500

if __name__ == "__main__":
    app.run(debug=True)
