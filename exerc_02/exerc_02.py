def obter_texto():
    texto = input("Digite um texto: ")
    return texto

def salvar_em_arquivo(texto):
    try:
        with open("./exerc_02/saida.txt", "w", encoding="utf-8") as arquivo:
            arquivo.write(texto)
        print("Texto salvo com sucesso no arquivo 'saida.txt'.")

    except FileNotFoundError as e:
        print("Erro: Arquivo não encontrado.")
        print(f"Exceção capturada: {e}")

    except PermissionError as e:
        print("Erro: Permissão negada para escrever no arquivo.")
        print(f"Exceção capturada: {e}")

    except Exception as e:
        print(f"Ocorreu um erro ao salvar o texto: {e}")

def main():
    texto_do_usuario = obter_texto()
    salvar_em_arquivo(texto_do_usuario)

if __name__ == "__main__":
    main()
