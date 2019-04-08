'''
        Project: Ordenação de Vetores
        Description: Ordenação por Flutuação
        Name: Júlio César de Carvalho Barros
        Email: jccb2@cin.ufpe.br
'''
def bubblesort(a):
    '''
        Ordenação por Flutuação
        Tempo de execução no melhor caso: @(n)
        Tempo de execução no pior caso: @(n²)
    '''
    f = True
    while f:
        f = False
        for i in range(len(a)-1):
            if a[i] > a[i + 1]:
                a[i], a[i + 1] = a[i + 1], a[i]
                f = True