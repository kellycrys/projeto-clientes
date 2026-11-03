from repository.cliente_repository import ClienteRepository

class ClienteService:
    def __init__(self):
        self.repository = ClienteRepository()

    def validar_cliente(self, dados):
        if not dados.get("nome"):
            return False, "O nome ou razão social é obrigatório."
        if not dados.get("email"):
            return False, "O e-mail de contacto é obrigatório."
        tipo = dados.get("tipo", "PF")
        if tipo == "PF" and not dados.get("cpf"):
            return False, "O CPF é obrigatório para Pessoa Física."
        if tipo == "PJ" and not dados.get("cnpj"):
            return False, "O CNPJ é obrigatório para Pessoa Jurídica."
        return True, "Dados válidos."

    def criar_cliente(self, dados):
        valido, mensagem = self.validar_cliente(dados)
        if not valido:
            return {"sucesso": False, "mensagem": mensagem}, 400
        novo_cliente = self.repository.inserir(dados)
        if novo_cliente:
            return {"sucesso": True, "cliente": novo_cliente}, 201
        return {"sucesso": False, "mensagem": "Erro ao gravar cliente na base de dados."}, 500

    def listar_clientes(self):
        return self.repository.buscar_todos()

    def filtrar_clientes(self, tipo=None, cidade=None, estado=None):
        return self.repository.buscar_filtrados(tipo, cidade, estado)

    def editar_cliente(self, id_cliente, dados):
        valido, mensagem = self.validar_cliente(dados)
        if not valido:
            return {"sucesso": False, "mensagem": mensagem}, 400
        atualizado = self.repository.atualizar(id_cliente, dados)
        if atualizado:
            return {"sucesso": True, "mensagem": "Cliente atualizado com sucesso."}, 200
        return {"sucesso": False, "mensagem": "Registo não localizado ou sem alterações efetuadas."}, 404

    def excluir_cliente(self, id_cliente):
        removido = self.repository.remover(id_cliente)
        if removido:
            return {"sucesso": True, "mensagem": "Cliente removido com sucesso."}, 200
        return {"sucesso": False, "mensagem": "Erro ao remover cliente ou registo inexistente."}, 404
