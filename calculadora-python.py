while True:
    try:
        n1 = int(input('Digite o primeiro número: '))
        n2 = int(input('Digite o segundo número: '))
    except ValueError:
        print('Atenção! Digite apenas números.')
        continue
    ope = input('Digite o operador: (+, -, *, /): ')

    if ope == '+':
        soma = (n1 + n2)
        print('O resultado é: {}'.format(soma))
    elif ope == '-':
        sub = (n1 - n2)
        print('O resultado é: {}'.format(sub))
    elif ope == '*':
        mult = (n1 * n2)
        print('O resultado é: {}'.format(mult))
    elif ope == '/':
        if n2 == 0:
            print('Zero não pode ser dividido, escolha outro número.')
        else:
            divi = (n1 / n2)
            print('O resultado é: {}'.format(divi))

    con = input('Deseja continuar? (S/N): ')
    if con in ('N', 'n'):
        break