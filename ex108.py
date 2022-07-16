"""Exercício Python 108: Adapte o código do desafio #107,
criando uma função adicional chamada moeda() que consiga mostrar
os números como um valor monetário formatado."""

from modulos import moeda

valor = float(input('Digite um valor: R$'))
aumento = int(input('Porcentagem do aumento: '))
desconto = int(input('Porcentagem do desconto: '))
valor_maior = moeda.aumentar(aumento, valor)
valor_menor = moeda.diminuir(desconto, valor)
valor_dobro = moeda.dobro(valor)
valor_metade = moeda.metade(valor)

print(f'\nValor digitado: ', end='')
moeda.moeda(valor)
print(f'Aumento de {aumento}%: ', end='')
moeda.moeda(valor_maior)
print(f'Desconto de {desconto}%: ', end='')
moeda.moeda(valor_menor)
print(f'Dobro: ', end='')
moeda.moeda(valor_dobro)
print(f'Metade: ', end='')
moeda.moeda(valor_metade)
