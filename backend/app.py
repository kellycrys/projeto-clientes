import os
from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv
from controllers.cliente_controller import cliente_bp

load_dotenv()

def create_app():
    app = Flask(__name__)
    CORS(app, resources={r"/api/*": {"origins": "*"}})
    app.register_blueprint(cliente_bp)

    @app.route("/", methods=["GET"])
    def index():
        return {"status": "ok", "mensagem": "API do Sistema de Clientes a correr com sucesso!"}, 200

    return app

if __name__ == "__main__":
    porta = int(os.getenv("PORT", 5000))
    aplicacao = create_app()
    print(f"Servidor backend a iniciar na porta {porta}...")
    aplicacao.run(host="0.0.0.0", port=porta, debug=True)
