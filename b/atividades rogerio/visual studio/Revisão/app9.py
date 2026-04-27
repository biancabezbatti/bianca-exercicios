#Exemplo com funções
'''
Exemplo de função para calcular uma tabuada
'''
def tabuada(numero):
    contador = 1
    while contador <=10:
        resultado = numero * contador
        print(numero , ' x ', contador, ' = ', resultado)
        contador +=1

numero = int(input('Informe um número'))
#chama a função
tabuada(numero)