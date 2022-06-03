"""Exercício Python 034: Escreva um programa que pergunte o
salário de um funcionário e calcule o valor do seu aumento.
Para salários superiores a R$1250,00, calcule um aumento de 10%.
Para os inferiores ou iguais, o aumento é de 15%."""


sal = float(input('Salário: '))
aum = float(0)
a = int(0)
if sal > 1250:
    aum = sal * 1.10
    a = 10
else:
    aum = sal * 1.15
    a = 15

print('Aumento de {}% \nSalário antigo: R${:.2f} \nSalário novo: R${:.2f}'.format(a, sal, aum))
