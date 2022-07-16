def leiadinheiro(msg):
    teste = False
    while teste is False:
        valor = str(input(msg)).replace(',', '.')
        if valor.isalpha() is True or valor.strip() == '':
            print(f'"{valor}" não é uma entrada válida!!')
        else:
            return float(valor)


def leiafloat(msg):
    while True:
        valor = str(input(msg)).replace(',', '.').strip()
        try:
            valor = float(valor)
        except Exception as e:
            print(f'Erro: {e.__class__}')
        else:
            return valor
