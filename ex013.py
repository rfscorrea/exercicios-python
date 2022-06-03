"""Exercício Python 013: Faça um algoritmo que leia o salário de um funcionário e
mostre seu novo salário, com 15% de aumento."""

salario = float(input('Digite seu salário: '))
salarioNovo = salario * 1.15
print('Salário antigo: R${:.2f} \nSalário novo com 15% de aumento: R${:.2f}'.format(salario, salarioNovo))
