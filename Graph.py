'''
    GRAPH
'''
class Vertice:
    def __init__(self,identifier):
        ''' Class constructor '''
        self.id = identifier
        self.c = 'white'
        self.π = None
        self.d = float('inf')
        self.f = float('inf')
        
    def __str__(self):
        ''' Default string returns '''
        return '({v.id}) '\
               'd: {v.d}, '\
               'f: {v.f}, '\
               'c: {v.c}, '\
               'π: {v.π}'.format(v = self)

    def __repr__(self):
        ''' Default representation method '''
        return '{}'.format(self.id)

    def __eq__(self, other):
        ''' Returns comparison x == y '''
        return self.id == other.id

class Graph:
    def __init__(self,args=[],weighted=False,directed=False):
        ''' Class constructor '''
        self.adjacents = {}
        self.vertices = {}
        self.directed = directed
        self.weighted = weighted
        self.time = 0
        #Adds in constructor
        if type(args) == type([]):
            for arg in args:
                self.addVertice(arg[0])
                self.addVertice(arg[1])
                if self.weighted:
                    self.addEdge(arg[0],arg[1],arg[2])
                else:
                    self.addEdge(arg[0],arg[1])
        if type(args) == type({}):
            for vertice, adjacents in args.items():
                self.addVertice(vertice)
                self.adjacents[vertice] = adjacents
                
    def __str__(self):
        ''' Default string returns '''
        result = 'List of Adjacency\n'
        for vertice, adjacents in self.adjacents.items():
            result += '{} : {}\n'.format(vertice, adjacents)
        return result

    def __repr__(self):
        ''' Default representation method '''
        return '{}'.format(self.adjacents)
    
    def addVertice(self,identifier):
        if not identifier in self.vertices:
            self.vertices[identifier] = Vertice(identifier)
            self.adjacents[identifier] = []

    def addEdge(self,origin,destiny,weight=None):
        if self.weighted:
            if not (destiny,weight) in self.adjacents[origin]:
                self.adjacents[origin].append((destiny,weight))
            if not self.directed:
                #if not (origin,weight) in self.adjacents[destiny]:
                self.adjacents[destiny].append((origin,weight))
        else:
            if not (destiny,weight) in self.adjacents[origin]:
                self.adjacents[origin].append(destiny)
            if not self.directed:
                #if not (origin,weight) in self.adjacents[destiny]:
                self.adjacents[destiny].append(origin)
    
    def remVertice(self,identifier):
        del self.vertices[identifier]
        del self.adjacents[identifier]
        for vertice in self.adjacents.values():
            i = 0
            while i < len(vertice):
                if (self.weighted and vertice[i][0] == identifier) or (vertice[i] == identifier):
                    del vertice[i]
                else:
                    i += 1
    
    def remEdge(self,origin,destiny,weight=None):
        i = 0
        while i < len(self.adjacents[origin]):
            if (self.weighted and self.adjacents[origin][i] == (destiny, weight)) or (self.adjacents[origin][i] == destiny):
                del self.adjacents[origin][i]
            else:
                i += 1
        if not self.directed:
            i = 0
            while i < len(self.adjacents[destiny]):
                if (self.weighted and self.adjacents[destiny][i] == (origin, weight)) or (self.adjacents[destiny][i] == origin):
                    del self.adjacents[destiny][i]
                else:
                    i += 1

    def isLinked(self,identifier1,identifier2):
        linked = False
        i = 0
        while i < len(self.adjacents[identifier1]) and not linked:
            if (self.weighted and self.adjacents[identifier1][i][0] == identifier2) or (self.adjacents[identifier1][i] == identifier2):
                linked = True
            else:
                i+= 1
        return linked

    def getInputDegree(self,identifier):
        count = 0
        for vertice in self.adjacents.values():
            for edge in vertice:
                if (self.weighted and edge[0] == identifier) or edge == identifier:
                    count += 1
        return count

    def getOutputDegree(self,vertice):
        return len(self.adjacents[vertice])

    def getDegree(self,vertice):
        if self.directed:
            return self.getInputDegree(vertice) + self.getOutputDegree(vertice)
        else:
            return self.getOutputDegree(vertice)

    def getAdjacents(self,vertice):
        return self.adjacents[vertice]
    
    def getSmallerEdge(self):
        weight = float('inf')
        smallers = []
        if self.weighted:
            for vertice, adjacents in self.adjacents.items():
                for edge in adjacents:
                    origin = self.vertices[vertice]
                    destiny = self.vertices[edge[0]]
                    if edge[1] == weight:
                        smallers.append((origin,destiny,edge[1]))
                    elif edge[1] < weight:
                        weight = edge[1]
                        smallers = [(origin,destiny,edge[1])]
            return smallers
        
    def getHigherEdge(self):
        weight = 0
        highers = []
        if self.weighted:
            for vertice, adjacents in self.adjacents.items():
                for edge in adjacents:
                    origin = self.vertices[vertice]
                    destiny = self.vertices[edge[0]]
                    if edge[1] == weight:
                        highers.append((origin,destiny,edge[1]))
                    elif edge[1] > weight:
                        weight = edge[1]
                        highers = [(origin,destiny,edge[1])]
            return highers

    def widthSearch(self,identifier):
        for v in self.vertices.values():
            v.c = 'white'
            v.d = float('inf')
            v.π = None
        s = self.vertices[identifier]
        s.c = 'gray'
        s.d = 0
        s.π = None
        Q = [s]
        while len(Q) > 0:
            u = Q.pop(0)
            for key in self.getAdjacents(u.id):
                v = self.vertices[key[0] if self.weighted else key]
                if v.c == 'white':
                    v.c = 'gray'
                    v.d = u.d + 1
                    v.π = u.id
                    Q.append(v)
            u.c = 'black'
        #print
        printTitle('WIDTH SEARCH({})'.format(s.id))
        for v in self.vertices.values():
            print('({v.id}) '\
                  'd: {v.d}, '\
                  'c: {v.c}, '\
                  'π: {v.π}'.format(v = v))

    def deepSearch(self,L=[]):
        for u in self.vertices.values():
            u.c = 'white'
            u.π = None
        self.time = 0
        for v in self.vertices.values():
            if v.c == 'white':
                self.__deepSearch(v, L)
        #print
        printTitle('DEEP SEARCH')
        for v in self.vertices.values():
            print('({v.id}) '\
                  'd: {v.d}, '\
                  'f: {v.f}, '\
                  'c: {v.c}, '\
                  'π: {v.π}'.format(v = v))
        
                  
    def __deepSearch(self,u,L=[]):
        self.time += 1
        u.d = self.time
        u.c = 'gray'
        for key in self.getAdjacents(u.id):
            v = self.vertices[key[0] if self.weighted else key]
            if v.c == 'white':
                v.π = u.id
                self.__deepSearch(v,L)
        u.c = 'black'
        self.time += 1
        u.f = self.time
        L.insert(0,u.id)


    def topologicalOrdering(self):
        L = []
        self.deepSearch(L)
        printTitle('TOPOLOGICAL ORDERING')
        print(L)
    
    def getAllEdges(self):
        E = []
        for v in self.vertices.values():
            heapSort(self.getAdjacents(v.id),1)
            for e in self.getAdjacents(v.id):
                edge = (v.id,e[0],e[1]) if self.weighted else (v.id,e)
                if not edge in E:
                    E.append(edge)
        heapSort(E, 2)
        return E

    def edgeNormalizer(self,edge):
        if not self.directed:
            origin = edge[0] if edge[0] <= edge[1] else edge[1]
            destiny = edge[0] if edge[0] > edge[1] else edge[1]
            edge = (origin,destiny,edge[2]) if self.weighted else (origin,destiny)
        return edge
    
    def prim(self,identifier):
        for v in self.vertices.values():
            v.d = float('inf')
            v.π = None
        self.vertices[identifier].d = 0
        Q = g.getAllEdges()
        while len(Q) != 0:
            u = Q.pop(0)
            for v in g.getAdjacents(u[0]):
                edge = (v[0],u[0],v[1])
                if edge in Q and v[1] < self.vertices[v[0]].d:
                    self.vertices[v[0]].π = u[0]
                    self.vertices[v[0]].d = v[1]
        #print
        printTitle('MINIMUM SPANNING TREE - PRIM({})'.format(identifier))
        P = []
        for v in self.vertices.values():
            if v.id != identifier:
                edge = (v.id,v.π,v.d)
                P.append(edge)
        print(P)
        
    def kruskal(self):
        F = {}
        for v in self.vertices.values():
            v.c = 'white'
            v.π = v.id
            F[v.π] = set()
        Q = g.getAllEdges()
        A = []
        i = 0
        while len(Q) != 0 and i != len(self.vertices) - 1:
            u = Q.pop(0)
            if self.vertices[u[0]].π != self.vertices[u[1]].π:
                if self.vertices[u[0]].c == 'white' and self.vertices[u[1]].c == 'white':
                    self.vertices[u[0]].c = 'black'
                    self.vertices[u[1]].c = 'black'
                    self.vertices[u[0]].π = u[0]
                    self.vertices[u[1]].π = u[0]
                    F[u[0]].add(u[0])
                    F[u[0]].add(u[1])
                    A.append(u)
                    i += 1
                elif self.vertices[u[0]].c == 'white' and self.vertices[u[1]].c == 'black':
                    self.vertices[u[0]].c = 'black'
                    self.vertices[u[0]].π = self.vertices[u[1]].π
                    F[u[1]].add(u[0])
                    A.append(u)
                    i += 1
                elif self.vertices[u[0]].c == 'black' and self.vertices[u[1]].c == 'white':
                    self.vertices[u[1]].c = 'black'
                    self.vertices[u[1]].π = self.vertices[u[0]].π
                    F[u[0]].add(u[1])
                    A.append(u)
                    i += 1
                elif self.vertices[u[0]].c == 'black' and self.vertices[u[1]].c == 'black':
                    for v in F[u[1]]:
                        self.vertices[v].π = self.vertices[u[0]].π
                    A.append(u)
                    i += 1
        #print
        printTitle('MINIMUM SPANNING TREE - KRUSKAL')
        print(A)
            
    def dijkstra(self,identifier):
        for v in self.vertices.values():
            v.d = float('inf')
            v.π = None
        self.vertices[identifier].d = 0
        Q = g.getAllEdges()
        while len(Q) != 0:
            u = Q.pop(0)
            for v in g.getAdjacents(u[0]):
                edge = (u[0],v[0],v[1])
                dist = v[1] if self.vertices[v[0]].π is None else self.vertices[self.vertices[v[0]].π].d + v[1]
                if edge in Q and dist < self.vertices[v[0]].d:
                    self.vertices[v[0]].π = u[0]
                    self.vertices[v[0]].d = dist
        #print
        printTitle('DIJKSTRA ({})'.format(identifier))
        for v in self.vertices.values():
            print('({v.id}) '\
                  'd: {v.d}, '\
                  'π: {v.π}'.format(v = v))				  

'''
        HEAP
'''
def heapSort(array,priority=None):
    ''' Order method based in Heap Structure '''
    h = Heap(array,priority)
    i = len(array) - 1
    while (i >= 0):
        array[i] = h.extract()
        i -= 1

class HeapItem():
    def __init__(self, priority, value):
        ''' Class constructor '''
        self.value = value
        self.priority = priority

    def __str__(self):
        ''' Returns string value '''
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
			
def printTitle(string):
    print('=' * 40 + '\n' + '{:^40}'.format(string) + '\n' + '=' * 40)                         
'''
    Debugger
'''
g = Graph([('v','r'),('r','s'),('s','w'),('w','t'),('w','x'),('t','x'),('t','u'),('x','u'),('x','y'),('u','y')])
printTitle('GRAPH')
print(
'''
    (r)-4-(s)   (t)-1-(u)
     |     |   / |   / |
     2     3  6  4  3  4
     |     | /   | /   |
    (v)   (w)-2-(x)-2-(y)
'''
)
g.widthSearch('s')

g = Graph([('u','v'),('u','x'),('x','v'),('v','y'),('y','x'),('w','y'),('w','z'),('z','z')],False,True)
printTitle('GRAPH')
print(
'''
    (u)→(v) (w)
     ↑   ↓ ↙ ↓ 
    (x) (y)←(z)
             ↺
'''
)
g.deepSearch()

g = Graph([(0,1),(0,2),(0,3),(1,3),(1,5),(1,6),(2,6),(3,5),(6,7),(4,7)],False,True)
printTitle('GRAPH')
print(
'''
    (0)→(2)→(6)←(4)
     ↓ ↘  ↗ ↓ ↙
    (3)←(1) (7)
     ↓ ↙
    (5)
'''
)
g.topologicalOrdering()

g = Graph([(0,2,9),(0,4,5),(0,3,1),(1,2,2),(1,3,2),(1,4,2),(2,4,3),(3,4,2)],True)
print('=' * 40 + '\n' + '{:^40}'.format('GRAPH') + '\n' + '=' * 40)
print(
'''
            (0)---9---(2)
             | \\5   3/ |
             1  >(4)<  2
             | /2   2\ |
            (3)---2---(1)
'''
)
g.prim(0)
g.kruskal()
g.dijkstra(0)
