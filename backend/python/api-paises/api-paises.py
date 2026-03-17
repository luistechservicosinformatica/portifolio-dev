import json
import sys
import requests

BASE_URL = "https://restcountries.com/v3.1"

cache = {}


def requisicao(endpoint):
    if endpoint in cache:
        return cache[endpoint]

    try:
        url = f"{BASE_URL}{endpoint}"
        resposta = requests.get(url, timeout=5)

        if resposta.status_code == 200:
            dados = resposta.json()
            cache[endpoint] = dados
            return dados
        else:
            print("erro:", resposta.status_code)

    except Exception as error:
        print("erro na requisição:", error)


def contagemDePaises():
    dados = requisicao("/all?fields=name")
    if dados:
        print(f"existem {len(dados)} países no mundo!")


def listarPaises():
    dados = requisicao("/all?fields=name")
    if dados:
        for pais in dados:
            print(pais["name"]["common"])


def buscarPorNome(nome):
    return requisicao(f"/name/{nome}")


def mostrarPopulacao(nome):
    dados = buscarPorNome(nome)
    if dados:
        for pais in dados:
            print(f"{pais['name']['common']}: {pais['population']} habitantes")


def mostrarMoedas(nome):
    dados = buscarPorNome(nome)
    if dados:
        for pais in dados:
            print(f"Moedas de {pais['name']['common']}")
            moedas = pais.get("currencies", {})
            for codigo, info in moedas.items():
                print(f"{info['name']} - {codigo}")


def buscarPorCapital(capital):
    dados = requisicao(f"/capital/{capital}")
    if dados:
        for pais in dados:
            print(pais["name"]["common"])


def buscarPorRegiao(regiao):
    dados = requisicao(f"/region/{regiao}")
    if dados:
        for pais in dados:
            print(pais["name"]["common"])


def buscarPorLinguagem(lingua):
    dados = requisicao(f"/lang/{lingua}")
    if dados:
        for pais in dados:
            print(pais["name"]["common"])


def ajuda():
    print()
    print("uso: python api_paises.py <acao> <valor>")
    print()
    print("acoes disponíveis:")
    print("contagem")
    print("listar")
    print("populacao <pais>")
    print("moeda <pais>")
    print("capital <capital>")
    print("regiao <regiao>")
    print("lingua <lingua>")
    print()


if __name__ == "__main__":
    if len(sys.argv) < 2:
        ajuda()
        sys.exit()

    acao = sys.argv[1]

    match acao:
        case "contagem":
            contagemDePaises()

        case "listar":
            listarPaises()

        case "populacao":
            if len(sys.argv) >= 3:
                mostrarPopulacao(sys.argv[2])
            else:
                print("informe o país")

        case "moeda":
            if len(sys.argv) >= 3:
                mostrarMoedas(sys.argv[2])
            else:
                print("informe o país")

        case "capital":
            if len(sys.argv) >= 3:
                buscarPorCapital(sys.argv[2])
            else:
                print("informe a capital")

        case "regiao":
            if len(sys.argv) >= 3:
                buscarPorRegiao(sys.argv[2])
            else:
                print("informe a região")

        case "lingua":
            if len(sys.argv) >= 3:
                buscarPorLinguagem(sys.argv[2])
            else:
                print("informe a língua")

        case _:
            print("ação inválida")
            ajuda()
