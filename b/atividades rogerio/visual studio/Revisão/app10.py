#Exemplo da classe carro
class Carro:
    def __init__(self,marca,modelo,ano,cor):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.cor = cor

    def exibir_informacoes(self):
        print('Informações do carro')
        print(f'Marca:{self.marca}')
        print(f'Modelo: {self.modelo}')
        print(f'Ano: {self.ano}' )
        print(f'Cor:{self.cor}')

#Criando o objeto da classe carro 
carro1 = Carro(marca='Toyota',modelo='Yaris', ano=2023,cor='cinza')
print('Exibindo informações do carro 1')
carro1.exibir_informacoes()
carro2 = Carro(marca='Chevrolet',modelo='Agile', ano=2012, cor='Preto')
print('Exibindo informações do carro 2')
carro2.exibir_informacoes()