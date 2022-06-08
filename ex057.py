"""Exercício Python 057: Faça um programa que leia o sexo de
uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado,
peça a digitação novamente até ter um valor correto."""

sexo = str(input('Digite seu sexo: [M] // [F]: ')).strip().lower()
while sexo != 'm' and sexo != 'f':
    print('VALOR INVÁLIDO!!')
    sexo = input('Digite seu sexo: [M] // [F]: ').strip().lower()
if sexo == 'm':
    print('Sexo: MASCULINO')
else:
    print('Sexo: FEMININO')
