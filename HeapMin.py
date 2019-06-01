'''
        Project: HeapMin
        Description: Implementação de uma estrutura heap e ordenação heap
        Name: Júlio César de Carvalho Barros
        Email: jccb2@cin.ufpe.br
'''

def heapSort(array):
    ''' Order method based in Heap Structure '''
    h = Heap(array)
    i = len(array) - 1
    while (i >= 0):
        array[i] = h.extractMin()
        i -= 1

class HeapItem():
    def __init__(self, priority, value):
        ''' Class constructor '''
        self.value = value
        self.priority = priority

    def __str__(self):
        return '(%s: %s)' % (self.value, self.priority)

    def __lt__(self, other):
        ''' Returns comparison x < y '''
        return self.priority < other.priority

    def __le__(self, other):
        ''' Returns comparison x <= y '''
        return self.priority <= other.priority

    def __eq__(self, other):
        ''' Returns comparison x == y '''
        return self.priority == other.priority

    def __ne__(self, other):
        ''' Returns comparison x != y or x <> y'''
        return self.priority != other.priority

    def __gt__(self, other):
        ''' Returns comparison x > y '''
        return self.priority > other.priority

    def __ge__(self, other):
        ''' Returns comparison x >= y '''
        return self.priority >= other.priority

class Heap():
    def __init__(self, array = []):
        ''' Class constructor or Build Heap'''
        i = len(array) // 2
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

    def extractMin(self):
        ''' Return and Extract maximum item of heap '''
        if self.array != []:
            smallest = self.array[0]
            self.array[0] = self.array[-1]
            self.array.pop()
            self.fixHeap(0)
            return smallest.value

    def fixHeap(self, i):
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
            self.fixHeap(smallest)

