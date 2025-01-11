nome = input("Digite o nome do jogo\n")
ano = int(input("Digite o ano do jogo\n"))
preco = float(input("Digite o preco do jogo\n"))
plano = bool(input("Esta incluso no serviço mensal?\n"))

print("###Dados do jogo###")
print("====================")
#Alternativa 1
# print("Nome do jogo:", nome)
# print("Ano do jogo:", ano)
# print("Preço do jogo:", preco)
# print("Incluso no plano:", plano)

#Alternativa 2

print(f"Nome do Jogo: {nome} \n Ano Lançamento: {ano} \n Preço do Jogo: {preco} \n Está incluso no serviço? {plano}")

