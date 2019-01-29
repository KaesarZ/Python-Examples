'''
        Project: Maior Divisor Comum
        Description: Calcula o maior divisor comum entre dois números inteiros recursivamente
'''
def mdc(a, b):
    ''' Retorna o maior divisor comum dos números paramentros '''
    if b == 0:
        return a
    else:
        return mdc(b, a % b)


def inputValidInt(label):
    ''' Retorna um inteiro válido digitado pelo usuário '''
    try:
        num = int(float(input(label)))
    except:
        print('Erro: a entrada precisa ser um inteiro.')
        return inputValidInt(label)
    return num

def main():
    ''' Função Inicial '''
    print('-------- MAIOR DIVISOR COMUM ---------')
    num1 = inputValidInt('Digite um número inteiro: ')
    num2 = inputValidInt('Digite outro número inteiro: ')
    print('mdc(' + str(num1) + ', ' + str(num2) + ') =', mdc(num1, num2))

main()
