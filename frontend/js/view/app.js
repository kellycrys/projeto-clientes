const controller = new ClienteController();

const formCliente = document.getElementById('formCliente');
const inputId = document.getElementById('clienteId');
const selectTipo = document.getElementById('tipoCliente');
const inputNome = document.getElementById('nome');
const campoPF = document.getElementById('campoPF');
const campoPJ = document.getElementById('campoPJ');
const inputCpf = document.getElementById('cpf');
const inputCnpj = document.getElementById('cnpj');
const inputWhatsapp = document.getElementById('whatsapp');
const inputEmail = document.getElementById('email');
const inputCidade = document.getElementById('cidade');
const inputEstado = document.getElementById('estado');
const btnLimpar = document.getElementById('btnLimpar');
const btnFiltrar = document.getElementById('btnFiltrar');
const btnListarTodos = document.getElementById('btnListarTodos');
const filtroCidade = document.getElementById('filtroCidade');
const corpoTabela = document.getElementById('corpoTabela');
const divMensagem = document.getElementById('mensagem');

selectTipo.addEventListener('change', () => {
  if (selectTipo.value === 'PF') {
    campoPF.style.display = 'block';
    campoPJ.style.display = 'none';
    inputCnpj.value = '';
  } else {
    campoPF.style.display = 'none';
    campoPJ.style.display = 'block';
    inputCpf.value = '';
  }
});

function lerFormulario() {
  const tipo = selectTipo.value;
  return {
    tipo: tipo,
    nome: inputNome.value.trim(),
    cpf: tipo === 'PF' ? inputCpf.value.trim() : null,
    cnpj: tipo === 'PJ' ? inputCnpj.value.trim() : null,
    whatsapp: inputWhatsapp.value.trim(),
    email: inputEmail.value.trim(),
    cidade: inputCidade.value.trim(),
    estado: inputEstado.value.trim().toUpperCase()
  };
}

function limparFormulario() {
  formCliente.reset();
  inputId.value = '';
  selectTipo.value = 'PF';
  campoPF.style.display = 'block';
  campoPJ.style.display = 'none';
  document.getElementById('btnSalvar').textContent = 'Salvar Cliente';
}

function mostrarMensagem(texto, sucesso = true) {
  divMensagem.textContent = texto;
  divMensagem.style.color = sucesso ? '#b45309' : '#b91c1c';
  setTimeout(() => { divMensagem.textContent = ''; }, 4000);
}

function mostrarClientes(listaClientes) {
  corpoTabela.innerHTML = '';
  if (!listaClientes || listaClientes.length === 0) {
    corpoTabela.innerHTML = `
      <tr>
        <td colspan="6" style="text-align: center; color: #64748b;">
          Nenhum cliente cadastrado no momento.
        </td>
      </tr>
    `;
    return;
  }

  listaClientes.forEach((cliente) => {
    const documento = cliente.tipo === 'PF' ? (cliente.cpf || '-') : (cliente.cnpj || '-');
    const linha = document.createElement('tr');
    linha.innerHTML = `
      <td>${cliente.id}</td>
      <td><strong>${cliente.tipo}</strong></td>
      <td>${cliente.nome}</td>
      <td>${documento}</td>
      <td>${cliente.cidade || '-'} / ${cliente.estado || '-'}</td>
      <td style="text-align: center;">
        <button class="btn-acao" onclick="prepararEdicao(${cliente.id})" style="padding: 4px 8px; font-size: 11px;">Editar</button>
        <button class="btn-secundario" onclick="confirmarExclusao(${cliente.id})" style="padding: 4px 8px; font-size: 11px; background-color: #ef4444;">Excluir</button>
      </td>
    `;
    corpoTabela.appendChild(linha);
  });
}

window.prepararEdicao = async function(id) {
  const lista = await controller.listar();
  const cliente = lista.find(c => c.id === id);
  if (cliente) {
    inputId.value = cliente.id;
    selectTipo.value = cliente.tipo;
    inputNome.value = cliente.nome;
    inputWhatsapp.value = cliente.whatsapp || '';
    inputEmail.value = cliente.email;
    inputCidade.value = cliente.cidade || '';
    inputEstado.value = cliente.estado || '';
    if (cliente.tipo === 'PF') {
      campoPF.style.display = 'block';
      campoPJ.style.display = 'none';
      inputCpf.value = cliente.cpf || '';
    } else {
      campoPF.style.display = 'none';
      campoPJ.style.display = 'block';
      inputCnpj.value = cliente.cnpj || '';
    }
    document.getElementById('btnSalvar').textContent = 'Atualizar Cliente';
    window.scrollTo({ top: 0, behavior: 'smooth' });
  }
};

window.confirmarExclusao = async function(id) {
  if (confirm(`Tem certeza de que deseja remover o cliente ${id}?`)) {
    const resultado = await controller.excluir(id);
    if (resultado && resultado.sucesso !== false) {
      mostrarMensagem('Cliente removido com sucesso!', true);
      carregarLista();
    } else {
      mostrarMensagem('Não foi possível excluir o cliente.', false);
    }
  }
};

formCliente.addEventListener('submit', async (evento) => {
  evento.preventDefault();
  const dados = lerFormulario();
  const id = inputId.value;
  let resposta = id ? await controller.editar(id, dados) : await controller.salvar(dados);
  if (resposta && resposta.sucesso !== false) {
    mostrarMensagem(id ? 'Cliente atualizado com sucesso!' : 'Cliente cadastrado com sucesso!', true);
    limparFormulario();
    carregarLista();
  } else {
    mostrarMensagem(resposta.mensagem || 'Erro ao processar dados do cliente.', false);
  }
});

btnLimpar.addEventListener('click', limparFormulario);

async function carregarLista() {
  const lista = await controller.listar();
  mostrarClientes(lista);
}

btnListarTodos.addEventListener('click', () => {
  filtroCidade.value = '';
  carregarLista();
});

btnFiltrar.addEventListener('click', async () => {
  const cidade = filtroCidade.value.trim();
  if (!cidade) {
    carregarLista();
    return;
  }
  const filtrados = await controller.filtrar(null, cidade, null);
  mostrarClientes(filtrados);
});

carregarLista();
