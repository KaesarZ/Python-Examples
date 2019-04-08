'''
        Project: Ordenação de Vetores
        Description: Comparação de tempo de execução
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


import random
import time

def comparation():
    for i in range(1, 6):
        a = [random.randint(0, 10 ** i) for _ in range(10 ** i)]
        b = a[:]
        c = a[:]
        d = a[:]
        e = a[:]
        f = a[:]

        #print('Array:', a)
        print('Lenght Array: {:14d}'.format(10 ** i))
        
        ini = time.time()
        insertionsort(c)
        end = time.time()
        print('InsertionSort: \t{:9.2f} ms'.format((end - ini) * 1000))

        ini = time.time()
        bubblesort(e)
        end = time.time()
        print('BubbleSort: \t{:9.2f} ms'.format((end - ini) * 1000))

        ini = time.time()
        selectionsort(e)
        end = time.time()
        print('SelectionSort: \t{:9.2f} ms'.format((end - ini) * 1000))

        ini = time.time()
        quicksort(b, 0, len(b) - 1)
        end = time.time()
        print('Quicksort: \t{:9.2f} ms'.format((end - ini) * 1000))

        ini = time.time()
        mergesort(d, 0, len(d) - 1)
        end = time.time()
        print('MergeSort: \t{:9.2f} ms'.format((end - ini) * 1000))

        print('-' * 30)

comparation()
