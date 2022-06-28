"""Exercício Python 105: Faça um programa que tenha uma função notas()
que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:

- Quantidade de notas
- A maior nota
- A menor nota
- A média da turma
- A situação (opcional)

Adicione também as docstrings dessa função para consulta pelo desenvolvedor."""


def notas(*a, stc=True):
    """
    :param a: notas da turma
    :param stc: mostrar situacao da turma
    :return: dicionario com informacoes da turma
    """
    maiornota = max(a)
    menornota = min(a)
    nnotas = len(a)
    media = sum(a) / len(a)

    if media >= 5:
        sit = 'APROVADOS'
    elif 3 <= media < 5:
        sit = 'RECUPERACAO'
    else:
        sit = 'REPROVADOS'

    info = {'Quantidade de notas': nnotas, 'Maior nota': maiornota,
            'Menor nota': menornota, 'Media': media}
    if stc:
        info['Situacao'] = sit

    return info


info = notas(5, 4, 3, 45, 10, 2, 1, 0.5, 3)
print(info)
