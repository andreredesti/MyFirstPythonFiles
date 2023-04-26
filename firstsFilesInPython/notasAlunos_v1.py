'''
Cálculo da média de aluno após receber 4 notas pela lista notas[] 
Uso de loop e array (vetor, lista)
'''
notas = []
soma = 0
print("Escreva a nota do aluno ")

for i in range (1, 5):
  notas = int(input("Informe a nota "))
  #notas = float(input("Informe a nota "))
  #notas = eval(input("Informe a nota "))
  soma = soma + notas
#soma = soma + notas[i]
print(f"A soma das notas do aluno foi: {soma}")

media = soma/4
print(f"A média do aluno foi: {media}")
if media > 6:
  print(f'Aluno aprovado com média: {media}')
else:
  print("Aluno reprovado")
