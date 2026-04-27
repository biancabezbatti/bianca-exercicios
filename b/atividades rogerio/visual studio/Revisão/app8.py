#adicionando dados no dicionário de forma dinâmica 
print('Dados do veículo')
marca = input('Informe a marca')
modelo = input('Informe o modelo')
placa = input('Informe a placa')

dados_veiculo = {
    'descricao':marca,
    'modelo':modelo,
    'placa':placa
}
print('Dados do motorista')
nome = input('Informe o nome')
cpf = int(input('Informe o cpf'))

dados_motorista = {
    'nome':nome,
    "cpf":cpf
}

print('Imprimindo dados do veículo')
print('Modelo: ',dados_veiculo['modelo'] )
print('marca: ',dados_veiculo['descricao'] )

print('Imprimindo dados do motorista')
print('Nome: ',dados_motorista['nome'] )
print('Cpf: ',dados_motorista['cpf'] )
