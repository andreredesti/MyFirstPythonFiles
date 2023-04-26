#Função saudação - recebido o nome pelo input
nome = input("Informe seu nome ")
def saudacao(nome):
    #nome = input("Informe seu nome")
    ##mensagem = "Olá, " + nome
    mensagem = "Olá, {nome}"
    #mensagem = f"Olá, {nome}"
    print(mensagem)

saudacao(nome)