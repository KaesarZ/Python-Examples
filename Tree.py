'''
        Project: Fatorial
        Description: Implementação de uma estrutura binary tree
        Name: Júlio César de Carvalho Barros
        Email: jccb2@cin.ufpe.br
'''

class _Node():
    def __init__(self, key, value):
        ''' Class constructor '''
        self.key = key
        self.value = value
        self.father = None
        self.left = None
        self.right = None

    def __str__(self):
        ''' Default string returns '''
        return '(%s:%s)' % (self.key, self.value)
            
class Tree():
    def __init__(self):
        ''' Class constructor '''
        self.root = None
        self.len = 0

    def __len__(self):
        return self.len

    def __str__(self):
        ''' Default string returns '''
        return '{ %s }' % self.__preOrder(self.root)

    def __repr__(self):
        ''' Default string returns '''
        return '{ %s }' % self.__preOrder(self.root)
    
    def __preOrder(self, node):
        result = ''
        if node != None:
            result += ' %s' % (node)
            result += str(self.__preOrder(node.left))
            result += str(self.__preOrder(node.right))
        return result

    def __inOrder(self, node):
        result = ''
        if node != None:
            result += str(self.__inOrder(node.left))
            result += ' %s' % (node)
            result += str(self.__inOrder(node.right))
        return result

    def __postOrder(self, node):
        result = ''
        if node != None:
            result += str(self.__postOrder(node.left))
            result += str(self.__postOrder(node.right))
            result += ' %s' % (node)
        return result
    
    def print(self, mode=0):
        if mode == 0:
            return '{%s }' % self.__preOrder(self.root)
        elif mode == 1:
            return '{%s }' % self.__inOrder(self.root)
        elif mode == 2:
            return '{%s }' % self.__postOrder(self.root)
        
    def insert(self, key, value=None):
        item = _Node(key, value)
        if self.root == None:
            self.root = item
        else:
            father = self.root
            while father != None:
                current = father
                if father.key > item.key:
                    father = father.left
                else:
                    father = father.right
            item.father = current
            if current.key > item.key:
                current.left = item
            else:
                current.right = item
        self.len += 1

    def search(self, key, mode=0):
        result = self.__searchRecursive(key, self.root)
        if result != None:
            return result
        else:
            raise KeyError(key)
        
    def __searchRecursive(self, key, current):
        if current == None or key == current.key:
            return current
        if key < current.key:
            return self.__searchRecursive(key, current.left)
        else:
            return self.__searchRecursive(key, current.right)

    def __replace(self, place, target):
        if place.father == None:
            self.root = target
        elif place == place.father.left:
            place.father.left = target
        else:
            place.father.right = target
        if target != None:
            target.father = place.father

    def minValue(self, current=None):
        if current == None:
            current = self.root
        while current.left != None:
            current = current.left
        return current

    def maxValue(self, current=None):
        if current == None:
            current = self.root
        while current.right != None:
            current = current.right
        return current
    
    def remove(self, key):
        found = self.search(key)
        if found != None:
            self.__remove(self.search(key))
            self.len -= 1
    
    def __remove(self, node):
        if node.left == None:
            self.__replace(node, node.right)
        elif node.right == None:
            self.__replace(node, node.left)
        else:
            successor = self.minValue(node.right)
            if successor.father != node:
                self.__replace(successor, successor.right)
                successor.right = node.right
                successor.right.father = successor
            self.__replace(node, successor)
            successor.left = node.left
            successor.left.father = successor
