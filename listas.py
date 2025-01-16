"""
Listas em Python 
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis: append, insert, pop, del, clear, extend, +
Create Read Update Delete

Criar,ler, alterar, remover

"""

string = 'ABCDE'

# lista = [123, True, 'Luiz Otávio', 1.2, []]



#Create Read Update Delete

#create
lista = [10, 20, 30, 40]

# #read
# print(lista[3])

# #Update
# lista[2] = 'Maria'

#delete
# deleta o ulmito
# limpar = lista.pop() 

# #DELETAR A POSIÇÃO ESCOLHIDA
# del lista[2]

# # Deletar a posição escolhida (caso o índice ainda exista)
# if len(lista) > 3:  # Verifica se o índice 3 existe na lista.
#     del lista[3]
# else:
#     print("O índice 3 não existe mais na lista.")

# # lista[-3] = 'Maria'
# print(lista)
# print(lista[2], type(lista[2]))


# lista.append('Luiz') # adiciona no final
# # nome = lista.pop() # remove o ultimo elemento

# print(lista)

#limpar a lista 
# lista.clear()

# adicionar no começo
# lista.insert(0, 5)

# #adicionar no meio
# lista.insert(2, 'banana')
# print(lista)

# #adicionar na ultima posição
# lista.append('Luiz')
# print(lista)

## concatenamdo listas 
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
lista3 = lista1 + lista2
print(lista3)
#extend
lista1.extend(lista2)
print(lista1)