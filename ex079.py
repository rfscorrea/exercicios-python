"""Exercício Python 079: Crie um programa onde o usuário
possa digitar vários valores numéricos e cadastre-os em uma
lista. Caso o número já exista lá dentro, ele não será adicionado.
No final, serão exibidos todos os valores únicos digitados, em ordem
crescente. """

lista = []
num = float(input('Digite o valor: '))
lista.append(num)
while True:
    resposta = input('Deseja digitar mais um valor? [s]/[n]: ')
    if resposta == 's':
        num = float(input('Digite o valor: '))
        if num in lista:
            print(f'O número {num} já está na lista')
        else:
            lista.append(num)
    elif resposta == 'n':
        break
lista.sort()
print(f'Valores digitados: {lista}')
