valorSacado = int(input('Valor sacado: '))
valor = valorSacado

while True:
    ced50 = valor // 50
    valor -= ced50*50
    if ced50 != 0:
        print(f'{ced50} notas de R$50')

    ced20 = valor // 20
    valor -= ced20 * 20
    if ced20 != 0:
        print(f'{ced20} notas de R$20')

    ced10 = valor // 10
    valor -= ced10 * 10
    if ced10 != 0:
        print(f'{ced10} notas de R$10')

    ced5 = valor // 5
    valor -= ced5 * 5
    if ced5 != 0:
        print(f'{ced5} notas de R$5')

    ced1 = valor // 1
    if ced1 != 0:
        print(f'{ced1} notas de R$1')
    break
