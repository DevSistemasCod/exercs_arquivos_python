def concatenar_arquivos(arquivo1, arquivo2, resultado):
    try:
        # Lê o conteúdo do primeiro arquivo
        with open(arquivo1, "r", encoding="utf-8") as arquivo1:
            conteudo_arquivo1 = arquivo1.read()

        # Lê o conteúdo do segundo arquivo
        with open(arquivo2, "r", encoding="utf-8") as arquivo2:
            conteudo_arquivo2 = arquivo2.read()

        # Concatena os conteúdos dos dois arquivos
        conteudo_concatenado = conteudo_arquivo1 + "\n" + conteudo_arquivo2

        # Salva o conteúdo concatenado no arquivo resultado.txt
        with open(resultado, "w", encoding="utf-8") as result_file:
            result_file.write(conteudo_concatenado)

        print(f"Conteúdo dos arquivos {arquivo1} e {arquivo2} concatenado com sucesso em {resultado}.")

    except FileNotFoundError as e:
        print(f"Erro: {e}")

    except Exception as e:
        print(f"Ocorreu um erro ao processar os arquivos: {e}")

if __name__ == "__main__":
    # Nomes dos arquivos
    arquivo1 = "./exerc_05/arquivo1.txt"
    arquivo2 = "./exerc_05/arquivo2.txt"
    resultado = "./exerc_05/resultado.txt"

    # Chama a função para concatenar os arquivos
    concatenar_arquivos(arquivo1, arquivo2, resultado)
