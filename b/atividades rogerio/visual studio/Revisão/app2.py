#Exemplo com estruturas de seleção
nome = input('Informe o nome')
idade = int(input('Informe a idade'))
if idade <=10:
  print('Você é criança')
elif idade > 10 and idade <= 19:
  print('Você é adolescente')
elif idade < 60:
  print('Você é adulto')
else:
    print('Você é idoso')
print('Seu nome é ', nome)
print('Sua idade é ', idade)
