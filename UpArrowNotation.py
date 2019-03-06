'''
        Project: Notação de Knuth
        Description: Retorna o resultado decimal dada uma expressão na notação de Knuth's Up-Arrow Notation
        Name: Júlio César de Carvalho Barros
        Email: jccb2@cin.ufpe.br
'''
num = int(input('Digite a base: '))
qnt = int(input('Digite a quantidade de up-arrows:'))
exp = int(input('Digite a quantidade de expoentes: '))

def multiarrows(num=0, qnt=1, exp=0):
    if qnt == 1:
        return num ** exp
    result = num
    for _ in range(exp - 1):
        result = multiarrows(num, qnt - 1, result)
    return result

print(multiarrows(num,qnt,exp))

