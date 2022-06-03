"""Exercício Python 043: Desenvolva uma lógica que leia o peso e a
altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e
mostre seu status, de acordo com a tabela abaixo:
- IMC abaixo de 18,5: Abaixo do Peso
- Entre 18,5 e 25: Peso Ideal
- 25 até 30: Sobrepeso
- 30 até 40: Obesidade
- Acima de 40: Obesidade Mórbida
"""

peso = float(input('Digite o peso em kg: '))
altura = float(input('Digite a altura em metros: '))
imc = peso / (altura * altura)
if imc < 18.5:
    print('Seu IMC é {} \nVocê está na categoria: abaixo do peso'.format(imc))
elif 18.5 <= imc <= 25:
    print('Seu IMC é {} \nVocê está na categoria: peso ideal'.format(imc))
elif 25 < imc <= 30:
    print('Seu IMC é {} \nVocê está na categoria: sobrepeso'.format(imc))
elif 30 < imc <= 40:
    print('Seu IMC é {} \nVocê está na categoria: obesidade'.format(imc))
else:
    print('Seu IMC é {} \nVocê está na categoria: obesidade mórbida'.format(imc))
