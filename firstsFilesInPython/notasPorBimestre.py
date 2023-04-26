print('Notas de Aluno por bimestre')
nome = input ('Qual seu nome: ')
notas = []
soma = 0
for i in range(1, 5):
  print(f"Notas do bimestre {i}")
  for i in range(1, 5):
    notas = int(input('informe nota: '))
  '''
  nota2 = float(input('Segunda nota: '))
  nota3 = float(input('Terceira nota: '))
  nota4 = float(input('Quarta nota: '))
'''
  soma = soma + notas[i]
  media = soma/4
#media = (nota1 + nota2 + nota3 + nota4)/4
#print(f"A média do aluno {nome} foi {media}")
if (media > 6):
  print(f"{nome}, Parabéns. Você foi aprovado com média igual a: {media}")
else:
  print(f"{nome}, Você foi reprovado. Sua média foi: {media}")