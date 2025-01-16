"""
Mutaveis = são dados que podem ter seus valores alterados
imutaveis = são dados que não podem ter seus valores alterados

Mutaveis:
- lista
- dicionario
- set

Imutaveis:
- str
- int
- float
- bool
- None
- tuple
- range
"""

lista_a = ['Luiz', 'Maria']
lista_b = lista_a.copy()

lista_a[0] = 'Qualquer coisa'
print(lista_a)
print(lista_b)
