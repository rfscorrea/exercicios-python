"""Exercício Python 019: Um professor quer sortear um dos seus
quatro alunos para apagar o quadro. Faça um programa que ajude ele,
lendo o nome dos alunos e escrevendo na tela o nome do escolhido."""

from random import choice

a1 = str(input('Aluno 1: '))
a2 = str(input('Aluno 2: '))
a3 = str(input('Aluno 3: '))
a4 = str(input('Aluno 4: '))
alunos = [a1, a2, a3, a4]
alunoSorteado = choice(alunos)
print('Alunos: \n{}, {}, {}, {} \nO(a) aluno(a) sorteado(a) foi o(a) {}!!!'.format(a1, a2, a3, a4, alunoSorteado))
