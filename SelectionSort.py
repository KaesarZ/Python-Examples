'''
        Project: Ordenação de Vetores
        Description: Ordenação por Seleção
        Name: Júlio César de Carvalho Barros
        Email: jccb2@cin.ufpe.br
'''  
def selectionsort(a):
    '''
        Ordenação por Seleção
        Tempo de execução no melhor caso: @(n²)
        Tempo de execução no pior caso: @(n²)
    '''
    for i in range(len(a) - 1) :
        m = i
        for j in range(i + 1, len(a)):
            if a[j] < a[m]:
                m = j
        if a[i] != a[m]:
            a[i], a[m] = a[m], a[i]
