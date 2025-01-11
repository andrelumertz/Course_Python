"""
1- Antecessor e Sucessor de um número
Escreva um programa em Python que leia um número e represente 
o número antecessor e sucessor desse número que 
foi lido, utilizando operadores de atribuição.



2- 

Média de 4 notas

Escreva um programa em Python que leia quatro números e calcule a média entre esses números
"""

numero = int(input("Digite um numero:"))

sucessor = numero + 1

antecessor = numero - 1

print(f" O numero {numero} tem o sucessor {sucessor} e o antecessor {antecessor}!")

numero1 = int(input("Digite um numero:"))
numero2 = int(input("Digite segundo numero"))
numero3 = int(input("Digite outro numero"))
numero4 = int(input("Digite outro numero"))

media = (numero1 + numero2 + numero3 + numero4) / 4

print(f"A media dessa operação é de {media}")