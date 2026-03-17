# 🌍 Countries API

## 🇺🇸 English Version

### Overview

A command-line application written in Python that retrieves real-time country data from a public API.  
It allows users to query multiple types of information such as number of countries, population, currencies, regions, languages, and more.

This project uses the **REST Countries API (v3.1)**:
https://restcountries.com/

---

### How the Program Works

The program is executed via terminal using command-line arguments.

Execution flow:
1. Reads input arguments (`sys.argv`)
2. Determines the requested action
3. Sends HTTP requests to the API
4. Caches responses to avoid repeated requests
5. Parses JSON responses
6. Displays formatted output

A simple in-memory cache is used to reuse API responses within the same execution.

---

### Usage

```bash
python3 api-paises.py <action> <value>
```

---

### Available Actions

#### Count all countries

```bash
python3 api-paises.py contagem
```

---

#### List all countries

```bash
python3 api-paises.py listar
```

---

#### Show population

```bash
python3 api-paises.py populacao <Country>
example: python3 api-paises.py populacao Brazil
```

---

#### Show currencies

```bash
python3 api-paises.py moeda <Country>
example: python3 api-paises.py moeda Brazil
```

---

#### Search by capital

```bash
python3 api-paises.py capital <Capital of Country>
example: python3 api-paises.py capital Berlin
```

---

#### Filter by region

```bash
python3 api-paises.py regiao <Region of World>
example: python3 api-paises.py regiao Europe
```

---

#### Search by language

```bash
python3 api-paises.py lingua <language>
example: python3 api-paises.py lingua portuguese
```

---

### API Endpoints Used

- All countries:
```
https://restcountries.com/v3.1/all
```

- Search by name:
```
https://restcountries.com/v3.1/name/{name}
```

- Search by capital:
```
https://restcountries.com/v3.1/capital/{capital}
```

- Filter by region:
```
https://restcountries.com/v3.1/region/{region}
```

- Search by language:
```
https://restcountries.com/v3.1/lang/{language}
```

---

### Data Handling

- API responses are JSON
- Parsed using Python's `json` module
- Key fields used:
  - `name.common`
  - `population`
  - `currencies`

---

### Error Handling

The program handles:

- Network failures
- Invalid inputs
- Missing arguments
- JSON parsing errors

Errors are displayed without interrupting execution.

---

### Requirements

- Python 3.10+
- requests

Install:

```bash
pip install requests
```

---

### Summary

This project demonstrates practical API consumption, CLI design, data caching, and JSON processing. It focuses on efficient data retrieval and flexible querying via terminal.



# 🇧🇷 Versão em Português

## Visão Geral

Aplicação em linha de comando (CLI) escrita em Python que consome uma API pública para obter dados de países em tempo real.

Permite consultar diversas informações como:
- Quantidade de países
- População
- Moedas
- Capitais
- Regiões
- Línguas

Utiliza a API:
https://restcountries.com/

---

## Como o Programa Funciona

O programa é executado via terminal com argumentos.

Fluxo de execução:
1. Lê os argumentos (`sys.argv`)
2. Identifica a ação solicitada
3. Faz requisições HTTP
4. Armazena respostas em cache
5. Processa JSON
6. Exibe os dados

Um cache simples em memória evita múltiplas requisições iguais.

---

## Uso

```bash
python3 api-paises.py <acao> <valor>
```

---

## Ações Disponíveis

### Contagem de países

```bash
python3 api-paises.py contagem
```

---

### Listar países

```bash
python3 api-paises.py listar
```

---

### População

```bash
python3 api-paises.py populacao <País>
exemplo: python3 api-paises.py populacao Brazil
```

---

### Moedas

```bash
python3 api-paises.py moeda <País>
exemplo: python3 api-paises.py moeda Brazil
```

---

### Buscar por capital

```bash
python3 api-paises.py capital <Capital do País>
exemplo: python3 api-paises.py capital Berlin
```

---

### Filtrar por região

```bash
python3 api-paises.py regiao <Região do Mundo>
exemplo: python3 api-paises.py regiao Europe
```

---

### Buscar por língua

```bash
python3 api-paises.py lingua <linguagem>
exemplo: python3 api-paises.py lingua english
```

---

## Endpoints Utilizados

- Todos os países:
```
https://restcountries.com/v3.1/all
```

- Buscar por nome:
```
https://restcountries.com/v3.1/name/{nome}
```

- Buscar por capital:
```
https://restcountries.com/v3.1/capital/{capital}
```

- Filtrar por região:
```
https://restcountries.com/v3.1/region/{regiao}
```

- Buscar por língua:
```
https://restcountries.com/v3.1/lang/{lingua}
```

---

## Estrutura dos Dados

Campos utilizados:
- `name.common`
- `population`
- `currencies`

---

## Tratamento de Erros

O programa trata:
- Falhas de rede
- Entradas inválidas
- Argumentos ausentes
- Erros de parsing

---

## Requisitos

- Python 3.10+
- requests

Instalação:

```bash
pip install requests
```

---

## Resumo

Projeto focado em consumo de API, uso de cache em memória e interação via CLI. Demonstra integração com serviços externos e processamento eficiente de dados.

