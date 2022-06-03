"""Exercício Python 044: Elabore um programa que calcule o valor a
ser pago por um produto, considerando o seu preço normal e condição de
pagamento:

- à vista dinheiro/cheque: 10% de desconto
- à vista no cartão: 5% de desconto
- em até 2x no cartão: preço formal
- 3x ou mais no cartão: 20% de juros
"""
print('Opções de pagamento \n[1] À vista dinheiro/cheque '
      '\n[2] À vista no cartão \n[3] Em até 2x no cartão \n[4] 3x ou mais no cartão')
a = int(input('Escolha da forma de pagamento: '))
precoi = float(input('Preço do produto: '))
precof = float(0)
if a == 1:
    precof = precoi * 0.90
    print('Você optou pela opção à vista dinheiro/cheque '
          '\nO produto de R${:.2f} passa a valer: R${:.2f}'.format(precoi, precof))
elif a == 2:
    precof = precoi * 0.95
    print('Você optou pela opção à vista no cartão '
          '\nO produto de R${:.2f} passa a valer: R${:.2f}'.format(precoi, precof))
elif a == 3:
    print('Você optou pela opção em até 2x no cartão '
          '\nO produto de R${:.2f} passa a valer: R${:.2f}'.format(precoi, precoi))
elif a == 4:
    precof = precoi * 1.20
    print('Você optou pela opção 3x ou mais no cartão '
          '\nO produto de R${:.2f} passa a valer: R${:.2f}'.format(precoi, precof))
else:
    print('Opção inválida!')
