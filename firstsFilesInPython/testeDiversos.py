#Testando números no Python
#a = 1; b = 0
"""a, b = 0, 1
while a < 10:
    print(a)
    a, b = b, a+b
  """
'''i = 0
nome = input("Escreva seu nome: ")
print(nome)


nota = int(input("Insira a primeira nota "))
for i in nota
'''
'''
numbers = [1, 2, 3, 4, 5]
for i in numbers:
  print(i)
 '''
'''
#Desse jeito dará erro
##for i = 1 to 10
 ## print(i)
 
frutas = ['Abacaxi', 'Morango', 'Uva']
for fruta in frutas:
  print(fruta)  
'''
'''
##nome = input("Insira seu nome ")
'''
'''
i = 0
junta = []
while i < 3:
  nome = str(input("Insira seu nome "))
  ##nome[i]
  print(nome[i])
  junta = str(junta) + nome[i]
  i += 1
  ##i++ esse tipo de incremento dá erro np Python
  #print(nome[i])
print(junta)
'''
'''
palavra = "PERNAMBUCO"
for i in palavra:
  print(i)
'''
'''
for numero in range(10):
   print(numero)
   '''
print('Notas de Aluno por bimestre')
nome = input ('Qual seu nome: ')
for bimestre in range(1, 5):
  print(f"Notas do bimestre {bimestre}")
  nota1 = float(input('Primeira nota: '))
  nota2 = float(input('Segunda nota: '))
  nota3 = float(input('Terceira nota: '))
  nota4 = float(input('Quarta nota: '))

media = (nota1 + nota2 + nota3 + nota4)/4
#print(f"A média do aluno {nome} foi {media}")
if (media > 6):
  print(f"{nome}, Parabéns. Você foi aprovado com média igual a: {media}")
else:
  print(f"{nome}, Você foi reprovado")
