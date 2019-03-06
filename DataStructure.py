'''
        Project: Wonderful Data Structure
        Description: Implementação de uma estrutura fila e pilha ligada
        Name: Júlio César de Carvalho Barros
        Email: jccb2@cin.ufpe.br

            Insert↓                     ↓Enqueue
       Denqueue ← * * * * * * * * * * * * → Pop
              Head|   ← Before|Next →   |Tail
'''        

class WonderfulObject():
    #Constructor
    def __init__(self, value):
        self.value = value
        self.next = None
        self.before = None

    def __str__(self):
        return str(self.value)
    
    #Getters and Setters
    def getValue(self):
        ''' Get value '''
        return self.value

    def setValue(self, value):
        ''' Set value '''
        return self.value
    
    def getNext(self):
        ''' Return next '''
        return self.next
    
    def setNext(self, obj):
        ''' Set next '''
        self.next = obj
        
    def getBefore(self):
        ''' Return before '''
        return self.before

    def setBefore(self, obj):
        ''' Set before '''
        self.before = obj
        
        
class WonderfulDataStructure():
    #Constructor
    def __init__(self):
        self.head = None
        self.tail = None
    
    #Methods
    def insert(self, obj):
        ''' Insert obj in head '''
        item = WonderfulObject(obj)
        if self.head == None and self.tail == None:
            self.head = item
            self.tail = item
        else:
            item.setNext(self.head)
            self.head.setBefore(item)
            self.head = item
    
    def enqueue(self, obj):
        ''' Insert obj in tail '''
        item = WonderfulObject(obj)
        if self.head == None and self.tail == None:
            self.head = item
            self.tail = item
        else:
            item.setBefore(self.tail)
            self.tail.setNext(item)
            self.tail = item
    
    def find(self, obj):
        ''' Find obj in structure'''
        if self.head == None and self.tail == None:
            return None
        else:
            current = self.head
            while current != None and current.getValue() != obj:
                current = current.getNext()
            return current

    def findLast(self, obj):
        ''' Find obj in structure'''
        if self.head == None and self.tail == None:
            return None
        else:
            current = self.tail
            while current != None and current.getValue() != obj:
                current = current.getBefore()
            return current

    def remove(self, obj):
        ''' Del first occurrence of obj in structure'''
        if self.head == None and self.tail == None:
            return False
        else:
            result = self.find(obj)
            if self.head == self.tail == result:
                self.head = None
                self.tail = None
            elif self.head == result:
                self.head.getNext().setBefore(None)
                self.head = self.head.getNext()
            elif self.tail == result:
                self.tail.getBefore().setNext(None)
                self.tail = self.tail.getBefore()
            elif result != None:
                result.getBefore().setNext(result.getNext())
                result.getNext().setBefore(result.getBefore())

    def removeLast(self, obj):
        ''' Del first occurrence of obj in structure'''
        if self.head == None and self.tail == None:
            return False
        else:
            result = self.findLast(obj)
            if self.head == self.tail == result:
                self.head = None
                self.tail = None
            elif self.head == result:
                self.head.getNext().setBefore(None)
                self.head = self.head.getNext()
            elif self.tail == result:
                self.tail.getBefore().setNext(None)
                self.tail = self.tail.getBefore()
            elif result != None:
                result.getBefore().setNext(result.getNext())
                result.getNext().setBefore(result.getBefore())
     
    def pop(self):
        ''' Remove tail obj '''
        if self.head == None and self.tail == None:
            return None
        elif self.head == self.tail:
            unique = self.tail
            self.head = None
            self.tail = None
            return unique
        else:
            last = self.tail
            self.tail.getBefore().setNext(None)
            self.tail = self.tail.getBefore()
            return last
    
    def denqueue(self):
        ''' Remove head obj '''
        if self.head == None and self.tail == None:
            return None
        elif self.head == self.tail:
            unique = self.head
            self.head = None
            self.tail = None
            return unique
        else:
            first = self.head
            self.head.getNext().setBefore(None)
            self.head = self.head.getNext()
            return first
        
    def size(self):
        ''' Return size '''
        if self.head == None and self.tail == None:
            return 0
        else:
            current = self.head
            count = 0
            while current != None:
                current = current.getNext()
                count += 1
            return count

    def __str__(self):
        ''' Print structure'''
        if self.head == None and self.tail == None:
            return '(WDS) {}'
        else:
            result = '(WDS) { '
            current = self.head
            result += '%s' % current
            while current != None:
                current = current.getNext()
                result += (', %s ' % current) if current != None else ''
            result += ' }'
            return result
        

def debugger():
    ''' debugger '''
    Breguinaite = WonderfulDataStructure()
    a = 2
    Breguinaite.insert(2)
    Breguinaite.insert(1)
    Breguinaite.insert(2)
    Breguinaite.insert(1)
    Breguinaite.insert(2)
    print(Breguinaite)
    print(Breguinaite.pop())
    print(Breguinaite)


debugger()
