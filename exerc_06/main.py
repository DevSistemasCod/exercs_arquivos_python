from funcionario import Funcionario

def main():
    lista_funcionarios = []

    while True:
        opcao = input("Digite 1 para cadastrar um novo funcionário ou 0 para sair: ")

        if opcao == "1":
            novo_funcionario = Funcionario.cadastrar_funcionario()
            lista_funcionarios.append(novo_funcionario)
        elif opcao == "0":
            Funcionario.salvar_funcionarios(lista_funcionarios)
            print("Funcionários cadastrados com sucesso. Programa encerrado.")
            break
        else:
            print("Opção inválida. Digite 1 para cadastrar ou 0 para sair.")


if __name__ == "__main__":
    main()
