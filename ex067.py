"""Exercício Python 067: Faça um programa que mostre a
tabuada de vários números, um de cada vez, para cada valor
digitado pelo usuário. O programa será interrompido quando o
número solicitado for negativo. """

while True:
    numero = int(input('Digite um número: '))
    if numero < 0:
        break
    print(f'=== Tabuada do {numero} ===')
    for i in range(1, 11):
        print(f'{numero:}x{i} = {numero*i}')
    print('=============================\n')
