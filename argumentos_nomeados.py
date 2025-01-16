"""
Argumentos nomeados e não nomeados em funções Python
Argumento nomeado tem nome com sinal de igual
Argumento nomeado é obrigatório

"""


def soma(a, b, c): #a e b são parametros
    print (a + b + c)


soma(4, 3, 2) ##passando os argumentos na ordem

#nomeado
soma(b=4, a=3, c=2) #passando os argumentos nomeados

#se eu nomear um argumento todos os outros também devem ser nomeados
soma(c=4, b=3, a=2)