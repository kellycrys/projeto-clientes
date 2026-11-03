from models.cliente import Cliente

class ClientePJ(Cliente):
    def __init__(self, nome, email, cnpj, razao_social=None, whatsapp=None, cidade=None, estado=None, id=None):
        super().__init__(nome, email, whatsapp, cidade, estado, id)
        self.tipo = "PJ"
        self.cnpj = cnpj
        self.razao_social = razao_social or nome

    def to_dict(self):
        dados = super().to_dict()
        dados["tipo"] = self.tipo
        dados["cnpj"] = self.cnpj
        dados["razao_social"] = self.razao_social
        dados["cpf"] = None
        return dados
