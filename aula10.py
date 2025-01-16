# entrada = input('[E]ntrar [S]air: ')
# senha_digitada = input('Senha: ')

# senha_permitida = '123456'

# if entrada == 'E' and senha_digitada == senha_permitida:
#     print('Entrar')
# else:
#     print('Sair')


# #avaliação de curto circuito
# print(True and False and True)

# ## Operador OR

# entrada = input('[E]ntrar [S]air: ')
# senha_digitada = input('Senha: ')

# senha_permitida = '123456' 

# if (entrada == 'E' or entrada == 'e') and senha_digitada == senha_permitida:
#     print('Entrar')
# else:
#     print('Sair')

## Operador NOT


# senha_permitida = '123456' 
# senha_digitada = input('Senha: ')

# ## not serve para inverter o valor

# if not senha_digitada != senha_permitida:
#     print('Entrar')
# else:
#     print('Sair')

#Operadoress in e not in

#strings são iteraveis
# 0 1 2 3 4 5
# O t á v i o
#-6-5-4-3-2-1

nome = 'Otavio'

print(nome[2])
print(nome[-4])

print(10 * '-')

print('a' in nome)

print('z' not in nome)