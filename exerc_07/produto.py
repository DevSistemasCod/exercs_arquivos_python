class Produto:
    def __init__(self, nome, preco, codigo, quantidade):
        self.__nome = nome
        self.__preco = preco
        self.__codigo = codigo
        self.__quantidade =  quantidade

    def calcular_preco_total(self):
        preco_total = self.__preco * self.__quantidade
        return preco_total
    
    def info_produto(self):
        print("Nome: ",self.__nome)
        print("Preço: ",self.__preco)
        print("Código: ",self.__codigo)
        print("Quantidade: ",self.__quantidade)

    
    def salvar_dados_do_produto(self):
        with open("./exerc_07/produtos.txt", "a", encoding="utf-8") as arquivo:
            arquivo.write(f"Nome: {self.__nome}\n")
            arquivo.write(f"Preço: {self.__preco}\n")
            arquivo.write(f"Código: {self.__codigo}\n")
            arquivo.write(f"Quantidade: {self.__quantidade}\n")
