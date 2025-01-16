"""
Imprecisão de ponto flutuante
Double-precision floating-point format IEEE 754
https://en.wikipedia.org/wiki/Double-precision_floating-point_format
https://docs.python.org/pt-br/3/tutorial/floatingpoint.html
"""

import decimal 
numero_1 = decimal.Decimal('0.1') #decimal.Decimal é uma classe que representa um numero decimal 
numero_2 = decimal.Decimal('0.7')
numero_3 = numero_1 + numero_2
print(numero_3)


numero_1 = 0.1
numero_2 = 0.7
numero_3 = numero_1 + numero_2
print(numero_3)


#formatado Obs. mais simples
print(f'{numero_3:.2f}') #dois numeros apos a ;

#outro metodo
numero_4 = round(numero_3, 2) #round arredonda o numero e esse 2 é a quantidade de casas decimais