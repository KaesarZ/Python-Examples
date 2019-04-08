'''
        Project: Ordenação de Vetores
        Description: Ordenação por Quick
        Name: Júlio César de Carvalho Barros
        Email: jccb2@cin.ufpe.br
'''  
def quicksort(a, p=None, r=None):
    ''' Ordenção Quick
        Tempo de execução no melhor caso: @(n ln n)
        Tempo de execução no pior caso: @(n²)
    '''
    def partition(a, p, r):
        x = a[r]
        i = p - 1
        for j in range(p, r):
            if a[j] <= x:
                i += 1
                a[i], a[j] = a[j], a[i]
        a[i + 1], a[r] = a[r], a[i + 1]
        return i + 1
    
    #Default overwrite
    p = p if p != None else 0
    r = r if r != None else len(a) - 1
    
    #Recursion step
    if p < r:
        q = partition(a, p, r)
        quicksort(a, p, q - 1)
        quicksort(a, q + 1, r)