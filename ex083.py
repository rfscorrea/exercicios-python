"""Exercício Python 083: Crie um programa onde o usuário digite
uma expressão qualquer que use parênteses. Seu aplicativo deverá
analisar se a expressão passada está com os parênteses abertos e
fechados na ordem correta."""

expr = str(input('Expressão: '))
pilha = []
for c in expr:
    if c == '(':
        pilha.append(c)
    elif c == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(c)
            pilha.append(c)
if len(pilha) == 0:
    print('Válido')
else:
    print('Inválido')
