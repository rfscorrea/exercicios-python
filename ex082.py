"""Exercício Python 082: Crie um programa que vai ler vários
números e colocar em uma lista. Depois disso, crie duas listas
extras que vão conter apenas os valores pares e os valores ímpares
digitados, respectivamente. Ao final, mostre o conteúdo das três
listas geradas."""

lista = [int(input('Número: '))]

while True:
    resposta = input('Deseja digitar mais? [s]/[n]: ')
    if resposta == 's':
        num = int(input('Número: '))
        lista.append(num)
    elif resposta == 'n':
        break

listaPar = lista[:]
listaImpar = lista[:]
tamanhoListaPar = tamanhoListaImpar = len(lista)


posicaoListaPar = 0
while True:
    # analisar os números numa mesma posição até um deles ser par
    if listaPar[posicaoListaPar] % 2 != 0 or listaPar[posicaoListaPar] == 0:
        del listaPar[posicaoListaPar]
        tamanhoListaPar -= 1

    # mudando variável para poder analisar a próxima posição
    else:
        posicaoListaPar += 1

    # se a posição a ser analisada é maior que o tamanho da lista a repetição para
    if posicaoListaPar > (tamanhoListaPar - 1):
        break

posicaoListaImpar = 0
while True:
    # analisar os números numa mesma posição até um deles ser impar
    if listaImpar[posicaoListaImpar] % 2 == 0 or listaImpar[posicaoListaImpar] == 0:
        del listaImpar[posicaoListaImpar]
        tamanhoListaImpar -= 1

    # mudando variável para poder analisar a próxima posição
    else:
        posicaoListaImpar += 1

    # se a posição a ser analisada é maior que o tamanho da lista a repetição para
    if posicaoListaImpar > (tamanhoListaImpar - 1):
        break

print(f'Lista: {lista}')
print(f'Listar par: {listaPar}')
print(f'Lista Ímpar: {listaImpar}')
