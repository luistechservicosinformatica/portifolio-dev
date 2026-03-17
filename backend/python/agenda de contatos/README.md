# 📇 Contact Manager (CLI)

## 🇺🇸 English Version

### Overview

A command-line contact management application written in Python.  
It allows users to manage a contact list with persistent storage using CSV and optional JSON support.

---

### How the Program Works

The application runs as an interactive CLI loop where the user selects actions from a menu.

At startup:
1. The program attempts to load data from a local file (`database.csv`)
2. The data is stored in memory using a dictionary (`AGENDA`)
3. The user interacts with the system through a menu-driven interface

All operations (add, edit, delete) update the in-memory data and immediately persist changes to disk.

---

### Data Structure

Contacts are stored in memory as a dictionary:

```json
{
    "John Doe": {
        "phone": "123456",
        "email": "john@email.com",
        "address": "Street A"
    }
}
```

- The contact name is used as a unique key
- Each contact contains three fields: phone, email, and address
- This structure allows fast lookup and updates

---

### Features

- Add new contacts
- Edit existing contacts
- Delete contacts
- Search for a contact by name
- List all contacts
- Export contacts to CSV or JSON
- Import contacts from CSV or JSON
- Automatic persistence to disk

---

### How to Use

#### Run the program

```bash
python main.py
```

---

#### Menu Options

```
[1] -> Show all contacts
[2] -> Search contact
[3] -> Add contact
[4] -> Edit contact
[5] -> Delete contact
[6] -> Export contacts
[7] -> Import contacts
[0] -> Exit
```

---

#### Adding a Contact

1. Select option `3`
2. Enter the contact name
3. Provide:
   - Phone
   - Email
   - Address

The contact is immediately saved.

---

#### Editing a Contact

1. Select option `4`
2. Enter an existing contact name
3. Provide new values

---

#### Searching for a Contact

1. Select option `2`
2. Enter the contact name

The program will display all stored information.

---

#### Exporting Data

1. Select option `6`
2. Choose format:
   - `csv`
   - `json`
3. Enter file name

---

#### Importing Data

1. Select option `7`
2. Choose format:
   - `csv`
   - `json`
3. Enter file name

Imported contacts are merged into the current dataset.

---

### File Persistence

#### Default Storage (CSV)

- File: `database.csv`
- Automatically loaded at startup
- Automatically updated after any modification

Each line follows the format:

```
name,phone,email,address
```

---

#### JSON Support

Used for manual import/export.

Example:

```json
{
    "Jhon Doe": {
        "phone": "654321",
        "email": "john@testemail.com",
        "address": "Street B"
    }
}
```

---

### Error Handling

The program handles common runtime issues such as:

- Missing files during import
- Invalid contact lookups
- Unexpected file read/write errors

Errors are displayed in the terminal without crashing the application.

---

### Behavior Notes

- Contact names are unique (used as keys)
- Importing data may overwrite existing contacts with the same name
- All changes are saved automatically (no manual save required)

---

### Summary

This project demonstrates a complete CRUD workflow in a CLI environment with persistent storage and data format interoperability (CSV and JSON). It is designed to be simple, functional, and easy to extend.



# 🇧🇷 Versão em Português

## Visão Geral

Aplicação de gerenciamento de contatos em linha de comando (CLI) escrita em Python.  
Permite gerenciar uma lista de contatos com persistência em arquivo CSV e suporte opcional a JSON.

---

## Como o Programa Funciona

A aplicação roda em um loop interativo no terminal onde o usuário escolhe ações através de um menu.

Ao iniciar:
1. O programa tenta carregar os dados do arquivo `database.csv`
2. Os dados são armazenados em memória em um dicionário (`AGENDA`)
3. O usuário interage com o sistema através de um menu

Todas as operações (adicionar, editar, excluir) atualizam os dados em memória e salvam automaticamente no disco.

---

## Estrutura de Dados

Os contatos são armazenados como um dicionário:

```python
{
    "joão": {
        "telefone": "123456",
        "email": "joao@email.com",
        "endereco": "Rua A"
    }
}
```

- O nome do contato é a chave única
- Cada contato possui telefone, email e endereço
- Permite acesso e atualização rápidos

---

## Funcionalidades

- Adicionar contatos
- Editar contatos
- Excluir contatos
- Buscar contato por nome
- Listar todos os contatos
- Exportar para CSV ou JSON
- Importar de CSV ou JSON
- Salvamento automático

---

## Como Usar

### Executar o programa

```bash
python main.py
```

---

### Menu

```
[1] -> Mostrar contatos
[2] -> Buscar contato
[3] -> Adicionar contato
[4] -> Editar contato
[5] -> Excluir contato
[6] -> Exportar contatos
[7] -> Importar contatos
[0] -> Sair
```

---

### Adicionar Contato

1. Escolha a opção `3`
2. Digite o nome
3. Informe:
   - Telefone
   - Email
   - Endereço

O contato é salvo automaticamente.

---

### Editar Contato

1. Escolha a opção `4`
2. Digite o nome existente
3. Informe os novos dados

---

### Buscar Contato

1. Escolha a opção `2`
2. Digite o nome

Os dados do contato serão exibidos.

---

### Exportar Dados

1. Escolha a opção `6`
2. Informe o formato:
   - `csv`
   - `json`
3. Informe o nome do arquivo

---

### Importar Dados

1. Escolha a opção `7`
2. Informe o formato:
   - `csv`
   - `json`
3. Informe o nome do arquivo

Os contatos importados são adicionados à agenda atual.

---

## Persistência

### CSV (padrão)

- Arquivo: `database.csv`
- Carregado automaticamente ao iniciar
- Atualizado automaticamente após alterações

Formato:

```
nome,telefone,email,endereco
```

---

### JSON

Usado para importação/exportação manual.

Exemplo:

```json
{
    "João da Silva": {
        "telefone": "654321",
        "email": "joao@emaildeteste.com",
        "endereco": "Rua B"
    }
}
```

---

## Tratamento de Erros

O programa trata erros comuns como:

- Arquivo não encontrado
- Contato inexistente
- Erros de leitura/escrita

Sem encerrar a aplicação.

---

## Observações

- O nome do contato é único
- Importação pode sobrescrever contatos existentes
- Não é necessário salvar manualmente

---

## Resumo

Este projeto demonstra um fluxo completo de CRUD em ambiente CLI com persistência em arquivo e suporte a múltiplos formatos de dados (CSV e JSON). Projetado para ser simples, funcional e fácil de evoluir.

