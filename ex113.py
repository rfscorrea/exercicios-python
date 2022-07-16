"""Exercício Python 113: Reescreva a função leiaInt() que fizemos no desafio 104,
incluindo agora a possibilidade da digitação de um número de tipo inválido. Aproveite
e crie também uma função leiaFloat() com a mesma funcionalidade."""


from utilidadesCeV import moeda, dado

n = dado.leiafloat('Valor: ')
print(f'{moeda.resumo(n, 10, 10)}')
