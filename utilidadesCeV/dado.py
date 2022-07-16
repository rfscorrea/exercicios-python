from utilidadesCeV import moeda


def leiadinheiro(msg):
    teste = False
    while teste is False:
        valor = str(input(msg)).replace(',', '.')
        if valor.isalpha() is True or valor.strip() == '':
            print(f'"{valor}" não é uma entrada válida!!')
        else:
            teste = True
            return float(valor)

