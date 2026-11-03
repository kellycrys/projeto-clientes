import os
from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv
from controllers.cliente_controller import cliente_bp

load_dotenv()

app = Flask(__name__)
CORS(app)
app.register_blueprint(cliente_bp)

@app.route("/", methods=["GET"])
def index():
    return {"status": "ok", "mensagem": "API do Sistema de Clientes a correr com sucesso!"}, 200

if __name__ == "__main__":
    porta = int(os.environ.get("PORT", 5000))
    print(f"Servidor backend a iniciar na porta {porta}...")
    app.run(host="0.0.0.0", port=porta, debug=True)
