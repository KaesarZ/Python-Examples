'''
        Project: Wonderful Data Structure
        Description: Implementação de uma estrutura fila e pilha ligada

              Push↓                     ↓Enqueue
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
    def push(self, obj):
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
            return False
        else:
            current = self.head
            while current.getValue() != obj and current != None:
                current = current.getNext()
            return current if current.getValue() == obj else False

    def findLast(self, obj):
        ''' Find obj in structure'''
        if self.head == None and self.tail == None:
            return False
        else:
            current = self.tail
            while current.getValue() != obj and current != None:
                current = current.getBefore()
            return current if current.getValue() == obj else False

    def remove(self, obj):
        ''' Del first occurrence of obj in structure'''
        if self.head == None and self.tail == None:
            return False
        else:
            result = self.find(obj)
            if (result != False):
                result.getBefore().setNext(result.getNext())
                result.getNext().setBefore(result.getBefore())
                del result
                return True
            else:
                return False

    def removeLast(self, obj):
        ''' Del first occurrence of obj in structure'''
        if self.head == None and self.tail == None:
            return False
        else:
            result = self.findLast(obj)
            if (result != False):
                result.getBefore().setNext(result.getNext())
                result.getNext().setBefore(result.getBefore())
                del result
                return True
            else:
                return False
     
    def pop(self):
        ''' Remove tail obj '''
        if self.head == None and self.tail == None:
            return False
        else:
            last = self.tail
            self.tail.getBefore().setNext(None)
            self.tail = self.tail.getBefore()
            return last
    
    def denqueue(self):
        ''' Remove head obj '''
        if self.head == None and self.tail == None:
            return False
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
            return '(None)'
        else:
            result = '(WDS) { '
            current = self.head
            result += '%s' % current
            while current != None:
                current = current.getNext()
                result += (', %s ' % current) if current != None else ''
            result += '}'
            return result
        

def debugger():
    ''' debugger '''
    wds = WonderfulDataStructure()
    a = 2
    wds.push(1)
    wds.push(a)
    wds.push(3)
    wds.enqueue('a')
    wds.enqueue('c')
    print(wds.removeLast(a))
    print(wds)

if __name__ == "__main__":
    debugger()

         
        
