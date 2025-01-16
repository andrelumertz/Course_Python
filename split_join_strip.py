"""
split e join com list e str
split - divide uma string
join - une uma string


"""

frase = 'Olha só que, coisa interessante'
lista_frases_cruas = frase.split(',')
lista_frases_cruas = frase.split(', ') #caso vc queira separar por espaço 

lista_frases = []

for i, frase in enumerate(lista_frases_cruas):
    lista_frases.append(lista_frases_cruas[i].strip()) # o strip remove os espaços em branco, o lstrip corta o lado esquerdo e o rstrip corta o lado direito

