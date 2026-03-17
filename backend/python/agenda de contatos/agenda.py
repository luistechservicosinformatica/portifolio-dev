import json

AGENDA = {}


def mostrarContatos():
    print()
    if AGENDA:
        for contato in AGENDA:
            buscarContato(contato)
    else:
        print(">>>> Agenda vazia")
    print()


def buscarContato(contato):
    try:
        print()
        print("Nome:", contato)
        print("Telefone:", AGENDA[contato]["telefone"])
        print("Email:", AGENDA[contato]["email"])
        print("Endereço:", AGENDA[contato]["endereco"])
        print("--------------------------------------------")
    except KeyError:
        print(">>>> Contato inexistente")
    except Exception as error:
        print(">>>> Erro inesperado")
        print(error)


def lerDetalhesContato():
    print()
    telefone = input("Telefone: ")
    email = input("Email: ")
    endereco = input("Endereço: ")
    return telefone, email, endereco


def incluirEditarContato(contato, telefone, email, endereco):
    AGENDA[contato] = {
        "telefone": telefone,
        "email": email,
        "endereco": endereco,
    }
    salvar()
    print()
    print(f">>>> {contato} salvo com sucesso")
    print()


def excluirContato(contato):
    try:
        AGENDA.pop(contato)
        salvar()
        print()
        print(f">>>> {contato} excluído com sucesso")
        print()
    except KeyError:
        print(">>>> Contato inexistente")
    except Exception as error:
        print(">>>> Erro inesperado")
        print(error)


def exportarContatos():
    print()
    formato = input("Formato (csv/json): ").lower().strip()
    nome = input("Nome do arquivo: ")

    try:
        if formato == "csv":
            with open(nome, "w") as arquivo:
                for contato in AGENDA:
                    d = AGENDA[contato]
                    arquivo.write(f"{contato},{d['telefone']},{d['email']},{d['endereco']}\n")
            print(">>>> Exportado em CSV")

        elif formato == "json":
            with open(nome, "w") as arquivo:
                json.dump(AGENDA, arquivo, indent=4)
            print(">>>> Exportado em JSON")

        else:
            print(">>>> Formato inválido")

    except Exception as error:
        print(">>>> Erro ao exportar")
        print(error)

    print()


def importarContatos():
    print()
    formato = input("Formato (csv/json): ").lower().strip()
    nome = input("Nome do arquivo: ")

    try:
        if formato == "csv":
            with open(nome, "r") as arquivo:
                for linha in arquivo:
                    nome, telefone, email, endereco = linha.strip().split(",")
                    incluirEditarContato(nome, telefone, email, endereco)

            print(">>>> Importado CSV")

        elif formato == "json":
            with open(nome, "r") as arquivo:
                dados = json.load(arquivo)

            for contato, info in dados.items():
                incluirEditarContato(
                    contato,
                    info["telefone"],
                    info["email"],
                    info["endereco"],
                )

            print(">>>> Importado JSON")

        else:
            print(">>>> Formato inválido")

    except FileNotFoundError:
        print(">>>> Arquivo não encontrado")
    except Exception as error:
        print(">>>> Erro ao importar")
        print(error)

    print()


def salvar():
    try:
        with open("database.csv", "w") as arquivo:
            for contato in AGENDA:
                d = AGENDA[contato]
                arquivo.write(f"{contato},{d['telefone']},{d['email']},{d['endereco']}\n")
    except:
        pass


def carregar():
    try:
        with open("database.csv", "r") as arquivo:
            for linha in arquivo:
                nome, telefone, email, endereco = linha.strip().split(",")
                AGENDA[nome] = {
                    "telefone": telefone,
                    "email": email,
                    "endereco": endereco,
                }

        print()
        print(">>>> Database carregado")
        print(f">>>> {len(AGENDA)} contatos")
        print()

    except FileNotFoundError:
        print()
        print(">>>> Nenhum database encontrado")
        print()

    except Exception as error:
        print(">>>> Erro ao carregar")
        print(error)


def imprimirMenu():
    print()
    print("==========================================")
    print("[1] -> Mostrar contatos")
    print("[2] -> Buscar contato")
    print("[3] -> Adicionar contato")
    print("[4] -> Editar contato")
    print("[5] -> Excluir contato")
    print("[6] -> Exportar contatos")
    print("[7] -> Importar contatos")
    print("[0] -> Sair")
    print("==========================================")


carregar()

while True:
    imprimirMenu()
    opcao = input("Opção: ")

    match opcao:
        case "1":
            mostrarContatos()

        case "2":
            contato = input("Nome: ")
            buscarContato(contato)

        case "3":
            contato = input("Nome: ")
            if contato in AGENDA:
                print(">>>> Já existe")
            else:
                telefone, email, endereco = lerDetalhesContato()
                incluirEditarContato(contato, telefone, email, endereco)

        case "4":
            contato = input("Nome: ")
            if contato in AGENDA:
                telefone, email, endereco = lerDetalhesContato()
                incluirEditarContato(contato, telefone, email, endereco)
            else:
                print(">>>> Não encontrado")

        case "5":
            contato = input("Nome: ")
            excluirContato(contato)

        case "6":
            exportarContatos()

        case "7":
            importarContatos()

        case "0":
            print()
            print(">>>> Encerrando")
            print()
            break

        case _:
            print(">>>> Opção inválida")
