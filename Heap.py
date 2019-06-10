'''
        Project: Heap
        Description: Implementação de uma estrutura heap e ordenação heap
        Name: Júlio César de Carvalho Barros
        Email: jccb2@cin.ufpe.br
'''
def heapSort(array,priority=None):
    ''' Order method based in Heap Structure '''
    h = Heap(array,priority)
    i = len(array) - 1
    while (i >= 0):
        array[i] = h.extract()
        i -= 1

class Heap():
    def __init__(self,array=[],priority=None,heapMin=False):
        ''' Build Heap '''
        self.min = heapMin
        i = len(array) // 2
        self.array = []
        #Adds in constructor
        for a in array:
            self.array.append(a if priority is None else HeapItem(a[priority],a))
        while i >= 0:
            if(self.min):
                self.fixHeapMin(i)
            else:
                self.fixHeapMax(i)
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

    def __len__(self):
        ''' Returns heap lenght '''
        return len(self.array)
    
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

    def extract(self):
        ''' Return and Extract root item of heap '''
        if self.array != []:
            root = self.array[0]
            self.array[0] = self.array[-1]
            self.array.pop()
            if(self.min):
                self.fixHeapMin(0)
            else:
                self.fixHeapMax(0)
            return root.value

    def fixHeapMin(self, i):
        ''' Reorder heap '''
        l = self.left(i)
        r = self.right(i)
        smallest = i
        if l < len(self.array) and self.array[l] < self.array[i]:
            smallest = l
        if r < len(self.array) and self.array[r] < self.array[smallest]:
            smallest = r
        if smallest != i:
            self.array[i], self.array[smallest] = self.array[smallest], self.array[i]
            self.fixHeapMin(smallest)

    def fixHeapMax(self, i):
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
            self.fixHeapMax(largest)
