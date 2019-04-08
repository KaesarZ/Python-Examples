'''
        Project: Ordenação de Vetores
        Description: Ordenação por Inserção
        Name: Júlio César de Carvalho Barros
        Email: jccb2@cin.ufpe.br
'''
def insertionsort(a):
    '''
        Ordenação por Inserção
        Tempo de execução no melhor caso: @(n)
        Tempo de execução no pior caso: @(n²)
    '''
    for j in range(len(a)):
        key = a[j]
        i = j - 1
        while i >= 0 and a[i] > key:
            a[i + 1] = a[i]
            i -= 1
        a[i + 1] = key