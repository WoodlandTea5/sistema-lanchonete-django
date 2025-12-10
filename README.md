# 🍔 Sistema Web de Lanchonete Django

Sistema completo de gestão de cardápio e produtos para lanchonetes, desenvolvido como **Projeto Prático Integrador**.

O sistema resolve o problema da atualização de preços e cardápios físicos, permitindo que o gerente controle tudo digitalmente e forneça dados para aplicativos externos via API.

---

## 🚀 Funcionalidades

### 🖥️ Para o Cliente e Gerente (Frontend)

- **Cardápio Digital:** Visualização moderna de produtos com fotos reais.
- **Gestão Visual:** Botões de edição e exclusão direto no cardápio (acesso rápido).
- **Upload de Fotos:** Cadastro de imagens dos lanches diretamente pelo navegador.

### ⚙️ Painel Administrativo e Backend

- **CRUD Completo:** Create, Read, Update, Delete de produtos e categorias.
- **API RESTful:** Endpoint JSON (`/api/produtos/`) pronto para integração com Mobile/Apps.
- **Banco de Dados MySQL:** Persistência robusta de dados.
- **Segurança:** Uso de variáveis de ambiente (`.env`) para proteção de credenciais.

---

## 🛠️ Tecnologias Utilizadas

- **Linguagem:** Python 3.11+
- **Framework Web:** Django 4.2 LTS
- **Banco de Dados:** MySQL (XAMPP/MariaDB)
- **Frontend:** Bootstrap 5, HTML5, CSS3
- **Formulários:** Django Crispy Forms
- **Imagens:** Biblioteca Pillow

---

## 📦 Como Rodar o Projeto

### Pré-requisitos

- Python instalado
- MySQL rodando (XAMPP recomendado)

### Passo a Passo

1. **Clone o repositório:**
   (Ou baixe o ZIP e extraia)
2. **Crie e ative o ambiente virtual:**

   ```bash
   python -m venv venv
   source venv/Scripts/activate  # Git Bash
   # ou
   .\venv\Scripts\Activate.ps1   # PowerShell
   ```



3. **Instale as dependências:**

   ```bash
   pip install -r requirements.txt
   ```
4. **Configure o arquivo `.env`:**
   Crie um arquivo chamado `.env` na raiz do projeto e configure:

   ```env
   SECRET_KEY=sua_chave_secreta_aqui
   DEBUG=True
   DB_NAME=lanchonete_db
   DB_USER=root
   DB_PASSWORD=
   DB_HOST=127.0.0.1
   DB_PORT=3306
   ```
5. **Prepare o Banco de Dados:**

   ```bash
   python manage.py migrate
   ```
6. **Inicie o Sistema:**

   ```bash
   python manage.py runserver
   ```

   Acesse: `http://127.0.0.1:8000`


## 🔗 Documentação da API

**Listar Todos os Produtos**

- **URL:** `/api/produtos/`
- **Método:** `GET`
- **Resposta (JSON):**
  ```json
  [
    {
      "id": 1,
      "nome": "X-Salada",
      "preco": 25.0,
      "categoria": "Lanches",
      "disponivel": true
    }
  ]
  ```

