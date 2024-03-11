def contar_linhas_arquivo(nome_arquivo):
    try:
        with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
            linhas = arquivo.readlines()
            return len(linhas)

    except FileNotFoundError as e:
        print(f"Erro: O arquivo '{nome_arquivo}' não foi encontrado.")
        print(f"Exceção capturada: {e}")
        return -1  # Retorna -1 para indicar erro

    except Exception as e:
        print(f"Ocorreu um erro ao contar as linhas: {e}")
        return -1  # Retorna -1 para indicar erro


def obter_qtd_linhas():
    nome_arquivo = "./exerc_03/dados.txt"
    total_linhas = contar_linhas_arquivo(nome_arquivo)

    if total_linhas != -1:
        print(f"O arquivo '{nome_arquivo}' contém {total_linhas} linhas.")


if __name__ == "__main__":
    obter_qtd_linhas()
