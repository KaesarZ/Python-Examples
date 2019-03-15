'''
        Project: Wonderful Data Structure
        Description: Implementação de uma estrutura fila ligada
        Name: Júlio César de Carvalho Barros
        Email: jccb2@cin.ufpe.br
'''
class QueueItem():
    #Constructor
    def __init__(self, value):
        self.value = value
        self.next = None
        
class Queue():
    #Constructor
    def __init__(self):
        self.first = None

    #Methods
    def enqueue(self, obj):
        ''' Insert obj in tail '''
        item = QueueItem(obj)
        if self.first == None:
            self.first = item
        else:
            last = self.first
            while last.next != None:
                last = last.next
            last.next = item

    def dequeue(self):
        ''' Remove obj in head '''
        if self.first != None:
            if self.first.next == None:
                unique = self.first
                self.first = None
                return unique.value
            else:
                dequeued = self.first
                self.first = self.first.next
                return dequeued.value
        else:
            return None

    def __str__(self):
        result = '(Queue) { '
        watch = self.first
        while watch != None:
            result += ('%s') % str(watch.value)
            result += ' ' if watch.next == None else ', '
            watch = watch.next
        result += '}'
        return result

def debugger():
    ''' debugger '''
    fila = Queue()

    fila.enqueue(1)
    print(fila)
    fila.dequeue()
    print(fila)
    fila.enqueue(2)
    print(fila)
    fila.enqueue(3)
    print(fila)
    print(fila.dequeue())
    print(fila)
    fila.dequeue()
    print(fila)
    fila.dequeue()
    print(fila)
    
debugger()
