'''
        Project: Fatorial
        Description: Implementação de uma estrutura heap e ordenação heap
        Name: Júlio César de Carvalho Barros
        Email: jccb2@cin.ufpe.br
'''

def heapSort(array):
    ''' Order method based in Heap Structure '''
    h = Heap(array)
    i = len(array) - 1
    while (i >= 0):
        array[i] = h.extractMax()
        i -= 1

class Heap():
    def __init__(self, list = []):
        ''' Class constructor or Build Heap'''
        i = len(list) // 2
        self.array = list[:]
        while i >= 0:
            self.fixHeap(i)
            i -= 1

    def __str__(self):
        ''' Default string returns '''
        length = len(self.array)
        result = '['
        for i in range(length):
            result += '%s' % str(self.array[i])
            result += ',' if i < (length - 1) else ''
        result += ']'
        return result

    def __repr__(self):
        ''' Default representation method '''
        length = len(self.array)
        result = '['
        for i in range(length):
            result += '%s' % str(self.array[i])
            result += ',' if i < (length - 1) else ''
        result += ']'
        return result
    
    def father(self, i):
        ''' Returns father '''
        return (i - 1)//2

    def left(self, i):
        ''' Returns left children '''
        return (2 * i + 1)

    def right(self, i):
        ''' Returns right children'''
        return (2 * i + 2)

    def insert(self, item):
        ''' Insert in heap '''
        self.array.append(item)
        i = len(self.array) - 1
        while i > 0 and self.array[self.father(i)] < item:
            self.array[i] = self.array[self.father(i)]
            i = self.father(i)
        self.array[i] = item

    def extractMax(self):
        ''' Return and Extract maximum item of heap '''
        if self.array != []:
            largest = self.array[0]
            self.array[0] = self.array[-1]
            self.array.pop()
            self.fixHeap(0)
            return largest

    def fixHeap(self, i):
        ''' Reorder heap '''
        l = self.left(i)
        r = self.right(i)
        largest = i
        if l < len(self.array) and self.array[l] > self.array[i]:
            largest = l
        if r < len(self.array) and self.array[r] > self.array[largest]:
            largest = r
        if largest != i:
            self.array[i], self.array[largest] = self.array[largest], self.array[i]
            self.fixHeap(largest)
