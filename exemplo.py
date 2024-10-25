import sqlite3

class Ecommerce:
    def __init__(self, db='db.sqlite3'):
       self.conn = sqlite3.connect
       self.menu()

    def menu(self):
        while True:
            print( '\n'
              '[1]- Create\n'
              '[2]- Read\n'
              '[3]- Update\n'
              '[4]- Delete\n'
              '[5]- Exit\n\n'
        )

        op = input('Escolha uma opção')

        match op:
            case '1':
                print('Create')
            case '2':
                print('Create')
            case '3':
                print('Create')
            case '4':
                print('Create')
            case '5':
                print('Create')
            case _:
                print('Escolha uma opção correta.')

    def create(self,tituloProduto,preco,descricao,imagemProduto,categoriaProduto,classProduto,exibirHome):
        pass

home = Ecommerce()