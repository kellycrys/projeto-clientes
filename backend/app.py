import os
from flask import Flask, jsonify
from flask_cors import CORS
from dotenv import load_dotenv

# Carregar variáveis de ambiente
load_dotenv()

# Importar controllers / rotas
from controllers.cliente_controller import cliente_bp

app = Flask(__name__)

# Habilitar CORS para permitir que o frontend (Netlify ou local) acesse a API
CORS(app)

# Registro dos Blueprints / Rotas
app.register_blueprint(cliente_bp, url_prefix='/api')

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "ok", "message": "API está funcionando perfeitamente!"}), 200

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
