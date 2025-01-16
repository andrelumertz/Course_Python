"""
Fatiamento de strings
012345678
Olá mundo
-987654321
Fatiamento [i:f:p] [::]
Obs.: a função len retorna a qtd
de caracteres da str

"""

variavel = 'Olá mundo'
print(variavel[4:]) #começa na posição 4 e vai até o final
print(variavel[4:8]) #fatiamento começa na posição 4 e vai até a 8, na 8 ele para
print(variavel[0:5:2]) #pula de 2 em 2
print(len(variavel)) #tamanho da string
print(variavel[-1])