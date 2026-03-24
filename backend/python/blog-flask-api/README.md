# 📝 Blog Pessoal (Flask + SQLAlchemy)

## 🇧🇷 Versão em Português

## 🚀 Visão Geral

Este é um sistema web de blog pessoal desenvolvido com **Python, Flask e SQLAlchemy**, permitindo a criação, edição e exclusão de posts com persistência em banco de dados.

O projeto foi estruturado com foco em organização, clareza de código e uma interface moderna e responsiva.

---

## 🧠 Arquitetura

```
Frontend (HTML + CSS + JS)
        ↓
Flask (Jinja2 Templates)
        ↓
SQLAlchemy (ORM)
        ↓
Banco de Dados (SQLite)
```

---

## 🔑 Funcionalidades

* Criar novos posts
* Editar posts existentes
* Excluir posts
* Listar todos os posts
* Persistência de dados com banco (SQLite)
* Interface moderna e responsiva
* Feedback visual e animações

---

## 🖥️ Interface

* Layout baseado em **cards**
* Inputs com foco visual
* Botões interativos
* Design inspirado em dashboards modernos
* Responsivo para dispositivos móveis

---

## 📸 Exemplo de Uso

### Criando um Post

1. Preencha:
   * Título
   * Autor
   * Conteúdo
2. Clique em **Postar**
3. O post será salvo no banco e exibido na tela

---

### Editando um Post

1. Clique em **Editar**
2. Atualize os campos
3. Clique em **Salvar**

---

### Excluindo um Post

1. Clique em **Excluir**
2. Confirme a ação

---

## Usando como uma API
### Rotas:
/api/post           --->  Método POST
```	json
	{
		"title":"<titulo>",
		"content":"conteudo",
		"author":"autor"		
	}
```



/api/post/id        --->  Método DELETE
	**SEM JSON!**


/api/post/id        --->  Método PUT
```	json
	{
		"title":"<titulo>",
		"content":"conteudo",
		"author":"autor"		
	}
```

---


## ⚙️ Como Executar

### 1. Clone o repositório

```
git clone github.com/luistechservicosinformatica/portifolio-dev
cd backend/python/blog-flask-api
```

### 2. Instale as dependências

```
pip install -r requirements.txt
```

---

### 3. Execute a aplicação

```
python3 app.py
```

---

### 4. Acesse no navegador

```
http://localhost:5000
```

---

## 📁 Estrutura do Projeto

```
/templates
    index.html
    edit.html

/static
    /css
        style.css
    /js
        main.js

__init__.py
config.py
models.py
routes.py
app.py
requirements.txt
```

---

## 🛠️ Tecnologias Utilizadas

* Python
* Flask
* SQLAlchemy
* SQLite
* HTML5
* CSS3
* JavaScript (Vanilla)
* Jinja2

---

## 📌 Destaques Técnicos

* Uso de **ORM com SQLAlchemy**
* Persistência real em banco de dados
* Separação entre lógica e apresentação
* Estrutura simples e escalável
* Interface consistente e moderna

---

## 📈 Possíveis Melhorias
* Paginação de posts
* Upload de imagens
* Dark mode

---

## 🧠 Resumo

Este projeto demonstra a construção de um sistema CRUD completo com Flask e persistência em banco de dados utilizando SQLAlchemy. Ele combina backend estruturado com uma interface moderna, sendo uma base sólida para aplicações web mais avançadas.

---
