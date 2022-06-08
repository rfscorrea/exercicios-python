"""Exercício Python 062: Melhore o DESAFIO 061, perguntando
para o usuário se ele quer mostrar mais alguns termos. O programa
encerrará quando ele disser que quer mostrar 0 termos."""

a1 = float(input('Primeiro termo: '))
r = float(input('Razão: '))
n = int(1)
print('=== PA ===')
while n != 10:
    print('{} → '.format(a1 + (n-1)*r), end='')
    n += 1
print('{}'.format(a1 + 9*r))


i = 1
while i != 0:
    i = int(input('\nQuer mostrar mais quantos termos?: '))
    if i == 0:
        break
    for i in range(1, i+1):
        print('{} → '.format((a1 + n * r) + (i-1) * r), end='')
    n += i
