from flask import Blueprint, request, jsonify
from services.cliente_service import ClienteService

cliente_bp = Blueprint("clientes", __name__, url_prefix="/api/clientes")
service = ClienteService()

@cliente_bp.route("", methods=["POST"])
def cadastrar():
    dados = request.get_json() or {}
    resposta, status_code = service.criar_cliente(dados)
    return jsonify(resposta), status_code

@cliente_bp.route("", methods=["GET"])
def listar_ou_filtrar():
    tipo = request.args.get("tipo")
    cidade = request.args.get("cidade")
    estado = request.args.get("estado")
    if tipo or cidade or estado:
        registos = service.filtrar_clientes(tipo, cidade, estado)
    else:
        registos = service.listar_clientes()
    return jsonify(registos), 200

@cliente_bp.route("/<int:id>", methods=["PUT"])
def atualizar(id):
    dados = request.get_json() or {}
    resposta, status_code = service.editar_cliente(id, dados)
    return jsonify(resposta), status_code

@cliente_bp.route("/<int:id>", methods=["DELETE"])
def excluir(id):
    resposta, status_code = service.excluir_cliente(id)
    return jsonify(resposta), status_code
