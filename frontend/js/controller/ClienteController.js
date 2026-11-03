class ClienteController {
  constructor() {
    this.apiUrl = 'http://localhost:5000/api/clientes';
  }

  async salvar(cliente) {
    try {
      const resposta = await fetch(this.apiUrl, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(cliente)
      });
      return await resposta.json();
    } catch (erro) {
      console.error('Erro ao salvar cliente:', erro);
      return { sucesso: false, mensagem: 'Não foi possível conectar ao servidor.' };
    }
  }

  async listar() {
    try {
      const resposta = await fetch(this.apiUrl);
      return await resposta.json();
    } catch (erro) {
      console.error('Erro ao listar clientes:', erro);
      return [];
    }
  }

  async filtrar(tipo, cidade, estado) {
    try {
      const params = new URLSearchParams();
      if (tipo) params.append('tipo', tipo);
      if (cidade) params.append('cidade', cidade);
      if (estado) params.append('estado', estado);
      const resposta = await fetch(`${this.apiUrl}?${params.toString()}`);
      return await resposta.json();
    } catch (erro) {
      console.error('Erro ao filtrar clientes:', erro);
      return [];
    }
  }

  async editar(id, cliente) {
    try {
      const resposta = await fetch(`${this.apiUrl}/${id}`, {
        method: 'PUT',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(cliente)
      });
      return await resposta.json();
    } catch (erro) {
      console.error('Erro ao editar cliente:', erro);
      return { sucesso: false, mensagem: 'Erro de comunicação ao atualizar.' };
    }
  }

  async excluir(id) {
    try {
      const resposta = await fetch(`${this.apiUrl}/${id}`, {
        method: 'DELETE'
      });
      return await resposta.json();
    } catch (erro) {
      console.error('Erro ao excluir cliente:', erro);
      return { sucesso: false, mensagem: 'Erro de comunicação ao excluir.' };
    }
  }
}
