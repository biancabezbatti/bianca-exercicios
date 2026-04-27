#Exemplo com dicionario 
'''
a estrutura de dicionario e usada
com valor e chave
'''
id_professor = 5
nome_professor = 'Rogerio'
email_professor = 'rogerio.santos@edu.sc.senai.br'
celular_professor= 4788988
id_aluno = 10
nome_aluno = ' Joao '
email_aluno = 'Joao@gmail.com'
celular_aluno = 47889687
id_uc = 8
nome_uc = 'Desenvolvimento de sistemas'
carga_horaria = 200
#agrupando em dicionário dados do professor
dados_professor = {
    'id': 5,
    'nome_professor': 'Rogério',
    'email_professor': 'rogerio.santos@edu.sc.senai.br',
    'celular_professsor':479999234,
}


#agrupando em dicionário dados do aluno
dados_aluno = {
    'id':10,
    'Nome': 'João',
    'email' : 'joao@gmail.com' ,
    'Celular' : 473434333
}

#agrupando em dcionário dados da U.C
dados_uc = {
    'id':8,
    'nome_uc':'Desenvolvimento de sistemas',
    'carga_horaria':200

}

#Exixibindo o nome do aluno
print('Nome do aluno')
print(dados_aluno['Nome'])

#Exibindo  o email do professor
print('Email do professor')
print(dados_professor['email_professor'])

#adicionando chave no dicionario do professor 
dados_professor['formacao'] = 'Especialização  - Pós Graduação'
print(dados_professor)

#exemplo imprimindo as chaves 
print(dados_aluno.keys())   
#exemplo imprimindo as chaves 
print(dados_aluno.values())    
#exemplo para imprimir o nome, chave 
#do dicionário
print(dados_aluno['Nome']) 
