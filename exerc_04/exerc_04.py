def converter_input_para_numeros(numeros_input):
    # Divide a string de entrada usando a vírgula como delimitador
    numeros_em_texto = numeros_input.split(',')
    numeros = []

    for num in numeros_em_texto:
        if num:
            numeros.append(float(num))

    return numeros

def escrever_numeros_em_arquivo():
    try:
        numeros_input = input("Digite uma sequência de números separados por vírgula: ")
        numeros = converter_input_para_numeros(numeros_input)

        # Salva os números no arquivo "números.csv"
        with open("./exerc_04/números.csv", "w", encoding="utf-8") as arquivo:
            for numero in numeros:
                arquivo.write(f"{numero},")
            print("Números salvos com sucesso no arquivo 'números.csv'.")

    except FileNotFoundError as e:
        print("Erro: Arquivo não encontrado.")
        print(f"Exceção capturada: {e}")

    except PermissionError as e:
        print("Erro: Permissão negada para escrever no arquivo.")
        print(f"Exceção capturada: {e}")

    except Exception as e:
        print(f"Ocorreu um erro: {e}")

def calcular_media_e_soma():
    try:
        # Lê os números do arquivo "números.csv"
        with open("./exerc_04/números.csv", "r", encoding="utf-8") as arquivo:
            # Lê o conteúdo do arquivo e divide em uma lista de strings usando a vírgula como delimitador
            numeros_em_texto = arquivo.read().split(',')

            # Cria uma lista vazia para armazenar os números convertidos
            numeros = []

            # Itera sobre cada string na lista de números em texto
            for num in numeros_em_texto:
                # Verifica se a string não está vazia antes de tentar converter para float
                if num:
                    # Converte a string para float e adiciona à lista de números
                    numeros.append(float(num))

            # Calcula a média e a soma
            if numeros:
                soma = sum(numeros)
                quantidade_numeros = len(numeros)
                media = soma / quantidade_numeros
            else:
                soma = 0
                quantidade_numeros = 0
                media = 0

            # Adiciona as linhas "Média: valor" e "Soma: valor" ao arquivo
            with open("./exerc_04/números.csv", "a", encoding="utf-8") as arquivo:
                arquivo.write(f"\nMédia: {media}\n")
                arquivo.write(f"Soma: {soma}\n")
                print(f"Média e soma adicionadas ao arquivo 'números.csv'.")

    except FileNotFoundError as e:
        print("Erro: Arquivo não encontrado.")
        print(f"Exceção capturada: {e}")

    except PermissionError as e:
        print("Erro: Permissão negada para escrever no arquivo.")
        print(f"Exceção capturada: {e}")

    except Exception as e:
        print(f"Ocorreu um erro ao calcular a média e a soma: {e}")

def main():
    escrever_numeros_em_arquivo()
    calcular_media_e_soma()

if __name__ == "__main__":
    main()
