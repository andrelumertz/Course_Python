"""
Repetiçoes 
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> Quando um código não tem fim

"""

# while True:
#     nome = input("Qual o seu nome? ")
#     print(f'Olá {nome}')

#     if nome == 'sair':
#         break


# contador = 0

# while contador <= 100:
#     contador += 1
    

#     if contador == 6:
#         print('Não vou mostrar o 6')
#         continue

#     if contador > 10 and contador < 27:
#         # print('Não vou mostrar o', contador)
#         print(f'Nao vou mostrar o {contador}')
#         continue

#     print(contador)
    
#     if contador == 40:
#         break

# print('Acabou')


senha_salva = '123456'
senha_digitada = ''
repeticoes = 0

while senha_salva != senha_digitada:
    senha_digitada = input(f'Sua senha ({repeticoes}x): ')

    repeticoes += 1