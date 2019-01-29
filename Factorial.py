'''
        Project: Fatorial
        Description: Calcula o fatorial recursivamente
'''
def fat(num):
    ''' Retorna o fatorial do número parâmetro recursivamente'''
    if num <= 1:
        return 1
    else:
        return num * fat(num - 1)

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
    print('-------------- FATORIAL --------------')
    num = inputValidInt('Digite um número inteiro: ')
    print(str(num)+'! =', fat(num))

main()
