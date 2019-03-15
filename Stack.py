'''
        Project: Wonderful Data Structure
        Description: Implementação de uma estrutura pilha ligada
        Name: Júlio César de Carvalho Barros
        Email: jccb2@cin.ufpe.br
'''
class StackItem():
    #Constructor
    def __init__(self, value):
        self.value = value
        self.over = None

class Stack():
    #Constructor
    def __init__(self):
        self.last = None

    #Methods
    def push(self, obj):
        ''' Insert obj in head '''
        item = StackItem(obj)
        if self.last == None:
            self.last = item
        else:
            item.over = self.last
            self.last = item

    def pop(self):
        ''' Remove head obj '''
        if self.last != None:
            if self.last.over == None:
                unique = self.last
                self.last = None
                return unique.value
            else:
                popped = self.last
                self.last = self.last.over
                return popped.value
        else:
            return None

    def __str__(self):
        result = '(Stack) { '
        watch = self.last
        while watch != None:
            result += ('%s') % str(watch.value)
            result += ' ' if watch.over == None else ', '
            watch = watch.over
        result += '}'
        return result

def debugger():
    ''' debugger '''
    pilha = Stack()

    print(pilha)
    pilha.push(1)
    print(pilha)
    pilha.pop()
    print(pilha)
    pilha.push(2)
    print(pilha)
    pilha.push(3)
    print(pilha)
    pilha.pop()
    print(pilha)
    
debugger()
                
