'''
        Project: Fibonacci
        Description: Calcula o n-zimo termo da sequencia de fibonacci recursivamente
        Name: Júlio César de Carvalho Barros
        Email: jccb2@cin.ufpe.br
'''
def fib(num, dic={}):
    ''' Retorna o valor do n-zimo termo da sequencia de fibonacci recursivamente'''
    if num < 2:
        return num
    elif num in dic:
        return dic[num]
    else:
        res = fib(num - 1, dic) + fib(num - 2, dic)
        if res not in dic:
            dic[num] = res
        return res
    
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
    print('------------- FIBONACCI --------------')
    num = inputValidInt('Digite um número inteiro: ')
    print('fibonacci(' + str(num) + ') =', fib(num))

main()
