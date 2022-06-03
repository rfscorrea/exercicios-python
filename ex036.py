"""Exercício Python 036: Escreva um programa para aprovar o empréstimo
bancário para a compra de uma casa. Pergunte o valor da casa, o salário
do comprador e em quantos anos ele vai pagar. A prestação mensal não pode
exceder 30% do salário ou então o empréstimo será negado."""

valor = float(input('Valor da casa: '))
salario = float(input('Salário: '))
anos = int(input('Em quantos anos vai pagar: '))
parcela = float(valor / (anos * 12))
if parcela > salario * 0.3:
    print('\033[31mEmpréstimo negado!')
else:
    print('\033[32mEmpréstimo aceito!')
print('\033[mValor da parcela mensal: \033[34mR${}'.format(parcela))


