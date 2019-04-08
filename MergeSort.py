'''
        Project: Ordenação de Vetores
        Description: Ordenação por Intercalação
        Name: Júlio César de Carvalho Barros
        Email: jccb2@cin.ufpe.br
'''  
def mergesort(a, p=None, r=None):
    '''
        Ordenação por Intercalação
        Tempo de execução no melhor caso: @(n lg n)
        Tempo de execução no pior caso: @(n lg n)
    '''
    def merge(a, s, m, e):
        l = a[s : (m + 1)]
        r = a[(m + 1) : (e + 1)]
        k = s
        i = 0
        j = 0
        while i < len(l) and j < len(r):
            if l[i] <= r[j]:
                a[k] = l[i]
                i += 1
            else:
                a[k] = r[j]
                j += 1
            k += 1
        while i < len(l):
            a[k] = l[i]
            i += 1
            k += 1
        while j < len(r):
            a[k] = r[j]
            j += 1
            k += 1
            
    #Default overwrite
    p = p if p != None else 0
    r = r if r != None else len(a) - 1
    
    #Recursion step
    q = (r + p) // 2
    if p < r:
        mergesort(a, p, q)
        mergesort(a, q + 1, r)
        merge(a, p, q, r)
