"""
enumerate - enumera iteraveis (indices)


"""

lista = ['Maria', 'Helena', 'Luiz']
lista.append('João')


# lista_enumerada = list(enumerate(lista, start=19))
# print(lista_enumerada)

for indice, nome in enumerate(lista): #desenpacotamento a lista usando o enumerate 
    # indice, noime = lista
    print(indice, nome)

