def ler_arquivo():
    # Obtém o caminho absoluto do arquivo "dados.txt"
    #caminho_absoluto = os.path.abspath("dados.txt")

    try:
        # Abre o arquivo "dados.txt" em modo leitura (r)
        with open("./exerc_01/dados.txt","r", encoding="utf-8") as arquivo:
            conteudo = arquivo.read()
            print(conteudo)

    except FileNotFoundError as e:
        print("O arquivo 'dados.txt' não foi encontrado.")
        print(f"Exceção capturada: {e}")

    except Exception as e:
        print(f"Ocorreu um erro: {e}")

if __name__ == "__main__":
    ler_arquivo()







