from produto import Produto

class ProdutoDigital(Produto):
    def __init__(self, nome, preco, codigo, quantidade, tamanho_em_MB, descricao):
        super().__init__(nome, preco, codigo, quantidade)
        self.__tamanho_em_MB = tamanho_em_MB
        self.__descricao = descricao

    def info_produto(self):
        super().info_produto()
        print("tamanho em MB: ",self.__tamanho_em_MB)
        print("Descrição: ",self.__descricao )
    
    def salvar_dados_do_produto(self):
        with open("./exerc_07/produtos.txt", "a", encoding="utf-8") as arquivo:
            arquivo.write("Tipo: Produto Digital\n")
            super().salvar_dados_do_produto()
            arquivo.write(f"Tamanho em MB: {self.__tamanho_em_MB}\n")
            arquivo.write(f"Descrição: {self.__descricao}\n\n")