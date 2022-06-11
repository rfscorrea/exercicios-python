"""Exercício Python 076: Crie um programa que tenha uma
tupla única com nomes de produtos e seus respectivos preços,
na sequência. No final, mostre uma listagem de preços, organizando
os dados em forma tabular."""

produtos_e_precos = ('produto1', 1.0, 'produto2', 2.0, 'produto3', 3.0,
                     'produto4', 4.0, 'produto5', 5.0, 'produto6', 6.0,
                     'produto7', 7.0, 'produto8', 8.0, 'produto9', 9.0,
                     'produto10', 10.0, 'produto11', 11.0, 'produto12', 12.0, )
tamanho = len(produtos_e_precos)

print('-'*40)
print(f'{"LISTA DE PREÇOS":^40}')
print('-'*40)
for c in range(0, tamanho, 2):
    print(f'{produtos_e_precos[c]:.<30}R${produtos_e_precos[c+1]:>7.2f}')
