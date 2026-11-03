from models.cliente import Cliente

class ClientePF(Cliente):
    def __init__(self, nome, email, cpf, whatsapp=None, cidade=None, estado=None, id=None):
        super().__init__(nome, email, whatsapp, cidade, estado, id)
        self.tipo = "PF"
        self.cpf = cpf

    def to_dict(self):
        dados = super().to_dict()
        dados["tipo"] = self.tipo
        dados["cpf"] = self.cpf
        dados["cnpj"] = None
        dados["razao_social"] = None
        return dados
