class Funcionario:
    def __init__(self, nome, cargo, salario):
        self.__nome = nome
        self.__cargo = cargo
        self.__salario = salario

    def __str__(self):
        return f"Nome: {self.__nome}, Cargo: {self.__cargo}, Salário: {self.__salario}\n"

    def cadastrar_funcionario():
        nome = input("Digite o nome do funcionário: ")
        cargo = input("Digite o cargo do funcionário: ")
        salario = float(input("Digite o salário do funcionário: "))

        funcionario = Funcionario(nome, cargo, salario)
        return funcionario


    def salvar_funcionarios(funcionarios):
        with open("./exerc_06/funcionarios.txt", "w", encoding="utf-8") as arquivo:
            for funcionario in funcionarios:
                arquivo.write(str(funcionario))
                arquivo.write("\n")
