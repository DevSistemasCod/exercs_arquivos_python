from produto_fisico import ProdutoFisico
from produto_digital import ProdutoDigital

def main():
    # Criando um produto físico
    produto_fisico = ProdutoFisico("Notebook", 2500.00, "12345", 2, 2.5, 0.3)
    produto_fisico.info_produto()
    produto_fisico.salvar_dados_do_produto()

    # Criando um produto digital
    produto_digital = ProdutoDigital("Pacote Office", 450.00, "67890", 1, 5500, "Licença digital")
    produto_digital.info_produto()
    produto_digital.salvar_dados_do_produto()

if __name__ == "__main__":
    main()