class Cliente:
    def __init__(self, nome, email, whatsapp=None, cidade=None, estado=None, id=None):
        self.id = id
        self.nome = nome
        self.email = email
        self.whatsapp = whatsapp
        self.cidade = cidade
        self.estado = estado

    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "email": self.email,
            "whatsapp": self.whatsapp,
            "cidade": self.cidade,
            "estado": self.estado
        }
