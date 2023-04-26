#Calcula a média de aluno - Versão 2
nome = input("Informe seu nome: ")
sobrenome = input("Informe seu sobrenome ")
nota1 = float(input("Informe a primeira nota: "))
nota2 = float(input("Informe a segunda nota: "))
print(nota1)
#media = float((nota1 + nota2)/2)
nomecompleto = nome + " " + sobrenome
media = (nota1 + nota2)/2

#print("O nome informado foi: ", nome)
#media = (nota1 + nota2)/2
print("O aluno: ",nome, sobrenome, "obteve as notas: ", nota1, " e ", nota2)
if media < 6:
  print("Você não foi aprovado")
elif media < 7:
    print("Você fará uma recuperação")
else: 
  print("A média final foi de: ", media, " Parabéns, ", nomecompleto)

