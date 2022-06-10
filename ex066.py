"""Exercício Python 066: Crie um programa que leia números inteiros
pelo teclado. O programa só vai parar quando o usuário digitar o valor 999,
que é a condição de parada. No final, mostre quantos números foram digitados
e qual foi a soma entre elas (desconsiderando o flag)."""

flag = 0
qntNumeros = 0
somaNumeros = 0
while flag != 999:
    numero = int(input('Digite um número: '))
    if numero == 999:
        break
    qntNumeros += 1
    somaNumeros += numero
print(f'Foram digitado {qntNumeros} números e a soma entre eles é {somaNumeros}.')
