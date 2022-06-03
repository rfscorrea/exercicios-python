"""Exercício Python 041: A Confederação Nacional de Natação precisa de
um programa que leia o ano de nascimento de um atleta e mostre sua
categoria, de acordo com a idade:
- Até 9 anos: MIRIM
- Até 14 anos: INFANTIL
- Até 19 anos: JÚNIOR
- Até 25 anos: SÊNIOR
- Acima de 25 anos: MASTER"""

ano = int(input('Ano: '))
idade = int(2022 - ano)
if idade <= 9:
    print('mirim')
elif 9 < idade <= 14:
    print('infantil')
elif 14 < idade <= 19:
    print('junior')
elif 19 < idade <= 25:
    print('senior')
else:
    print('master')
    