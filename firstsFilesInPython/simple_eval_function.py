expr = "(2 * 5 + (3 - 5)) / 2"
resultado = eval(expr)

print(resultado)

print("#############")

## Usando junto a condicionais
expressao = "w if w > 0 else -w"
w = 0
result = eval(expressao)

#w = 5
print(result)

w = -5
result = eval(expressao)
print(result)

print("#############")

number = 9

square_number = eval("number * number")

print(square_number)

h = 5
print(eval("h * 8"))

#####################
##Não é aconselhável usar o eval recebendo dados pelos usuário
#como em: numero = eval(input('Informe um número: '))

numero = eval(input('Informe um número: '))

print(numero)

if 5 > 2:
 print("Five is greater than two!")  
if 5 > 2:
        print("Five is greater than two!") 
