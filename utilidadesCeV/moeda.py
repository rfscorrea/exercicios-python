def moeda(valor, cifrao='R$'):
    return f'{cifrao}{valor:.2f}'.replace('.', ',')


def aumentar(a=0, valor=0, moedas=True):
    aum = (1 + (a/100)) * valor
    if moedas is True:
        return moeda(aum)
    else:
        return aum


def diminuir(a=0, valor=0, moedas=True):
    dim = valor * (1 - (a/100))
    if moedas is True:
        return moeda(dim)
    else:
        return dim


def dobro(valor, moedas=True):
    result = valor * 2
    if moedas is True:
        return moeda(result)
    else:
        return result


def metade(valor, moedas=True):
    result = valor / 2
    if moedas is True:
        return moeda(result)
    else:
        return result


def resumo(valor=0, a=0, b=0):
    return f'Valor: {moeda(valor)}' \
           f'\n{a}% de aumento: {aumentar(a, valor, True)}' \
           f'\n{b}% de desconto: {diminuir(b, valor, True)}' \
           f'\nDobro: {dobro(valor, True)}' \
           f'\nMetade: {metade(valor, True)}'
