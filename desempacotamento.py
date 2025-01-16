"""
Introdução ao desempacotamento e tuplas
"""

nome1, nome2, nome3 = ['Maria', 'Helena', 'Luiz']
# print(nome2)

# quando voce quer desempacotar so um elemento da lista
# nome1, *resto = ['Maria', 'Helena', 'Luiz']
nome1, *_ = ['Maria', 'Helena', 'Luiz']


_, _, nome, *_ = ['Maria', 'Helena', 'Luiz', 'Joana']

print(nome)