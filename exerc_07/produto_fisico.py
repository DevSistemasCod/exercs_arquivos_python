from produto import Produto

class ProdutoFisico(Produto):
    def __init__(self, nome, preco, codigo,  quantidade, peso, altura):
        super().__init__(nome, preco, codigo, quantidade)
        self.__peso = peso
        self.__altura = altura

    def calcular_preco_total(self):
        return super().calcular_preco_total() + (0.05 * super().calcular_preco_total())
    
    def info_produto(self):
        super().info_produto()
        print("Peso: ",self.__peso)
        print("Altura: ",self.__altura)

    def salvar_dados_do_produto(self):
        with open("./exerc_07/produtos.txt", "a", encoding="utf-8") as arquivo:
            arquivo.write("Tipo: Produto Físico\n")
            super().salvar_dados_do_produto()
            arquivo.write(f"Peso: {self.__peso}\n")
            arquivo.write(f"Altura: {self.__altura}\n\n")