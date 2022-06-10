"""Exercício Python 069: Crie um programa que leia a idade e o sexo de
várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar
se o usuário quer ou não continuar. No final, mostre:

A) quantas pessoas tem mais de 18 anos.
B) quantos homens foram cadastrados.
C) quantas mulheres tem menos de 20 anos. """

adultos = 0
homens = 0
mulheres = 0
while True:
    idade = int(input('Idade: '))
    if idade >= 18:
        adultos += 1
    sexo = input('Sexo [M][F]: ').lower().strip()
    if sexo == 'm':
        homens += 1
    elif sexo == 'f' and idade < 20:
        mulheres += 1
    flag = input('Deseja cadastrar mais um cliente? [s][n]: ').strip().lower()
    if flag == 'n':
        break
print(f'\nPessoas com mais de 18 anos: {adultos}'
      f'\nHomens: {homens} \nMulheres com menos de 20 anos: {mulheres}')
