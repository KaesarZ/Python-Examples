'''
        Project: Graph
        Description: Implementation by adjacency list
        Name: Júlio César de Carvalho Barros
        Email: jccb2@cin.ufpe.br
'''
class Vertice:
    def __init__(self,id):
        self.id = id
        self.color = 'white'
        self.π = None
        self.d = float('inf')
        self.f = float('inf')
        
    def __str__(self):
        return '({}) color: {}, d: {}, f: {}, π: {}'.format(self.id,self.color,self.d,self.f,self.π.id if self.π != None else None)

    def __repr__(self):
        return '{}'.format(self.id)

    def __eq__(self, other):
        return self.id == other.id if type(self) == type(other) else self.id == other

class Edge:
    def __init__(self,origin,destiny,weight=None,directed=False):
        self.origin = origin
        self.destiny = destiny
        self.weight = weight
        self.directed = directed

    def __repr__(self):
        if self.weight == None:
            return '({},{})'.format(self.origin.id, self.destiny.id)
        else:
            return '({},{},{})'.format(self.origin.id, self.destiny.id, self.weight)

class Graph:
    def __init__(self,args=[],weighted=False,directed=False):
        self.adjacents = {}
        self.vertices = {}
        self.directed = directed
        self.weighted = weighted
        self.time = 0
        #Adds in constructor
        for arg in args:
            self.addVertice(arg[0])
            self.addVertice(arg[1])
            if self.weighted:
                self.addEdge(arg[0],arg[1],arg[2])
            else:
                self.addEdge(arg[0],arg[1])
                
    def __str__(self):
        result = 'List of Adjacency\n'
        for vertice, adjacents in self.adjacents.items():
            result += '{} : {}\n'.format(vertice, adjacents)
        return result

    def __repr__(self):
        result = 'List of Adjacency\n'
        for vertice, adjacents in self.adjacents.items():
            result += '{} : {}\n'.format(vertice, adjacents)
        return result
    
    def addVertice(self,id):
        if not id in self.vertices:
            self.vertices[id] = Vertice(id)
            self.adjacents[id] = []

    def addEdge(self,origin,destiny,weight=None):
        if self.weighted:
            self.adjacents[origin].append((destiny,weight))
            if not self.directed:
                self.adjacents[destiny].append((origin,weight))
        else:
            self.adjacents[origin].append(destiny)
            if not self.directed:
                self.adjacents[destiny].append(origin)
    
    def remVertice(self,id):
        del self.vertices[id]
        del self.adjacents[id]
        for vertice in self.adjacents.values():
            i = 0
            while i < len(vertice):
                if (self.weighted and vertice[i][0] == id) or (vertice[i] == id):
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

    def isLinked(self,id1,id2):
        linked = False
        i = 0
        while i < len(self.adjacents[id1]) and not linked:
            if (self.weighted and self.adjacents[id1][i][0] == id2) or (self.adjacents[id1][i] == id2):
                linked = True
            else:
                i+= 1
        return linked

    def getInputDegree(self,id):
        count = 0
        for vertice in self.adjacents.values():
            for edge in vertice:
                if (self.weighted and edge[0] == id) or edge == id:
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
                        smallers.append(Edge(origin,destiny,edge[1]))
                    elif edge[1] < weight:
                        weight = edge[1]
                        smallers = [Edge(origin,destiny,edge[1])]
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
                        highers.append(Edge(origin,destiny,edge[1]))
                    elif edge[1] > weight:
                        weight = edge[1]
                        highers = [Edge(origin,destiny,edge[1])]
            return highers

    def widthSearch(self,id):
        for v in self.vertices.values():
            v.color = 'white'
            v.d = float('inf')
            v.π = None
        s = self.vertices[id]
        s.color = 'gray'
        s.d = 0
        s.π = None
        Q = [s]
        while len(Q) > 0:
            u = Q.pop(0)
            for key in self.getAdjacents(u.id):
                v = self.vertices[key[0] if self.weighted else key]
                if v.color == 'white':
                    v.color = 'gray'
                    v.d = u.d + 1
                    v.π = u
                    Q.append(v)
            u.color = 'black'
        self.__printWidthSearch()

    def __printWidthSearch(self):
        print('Width Search:')
        for v in self.vertices.values():
            print('({}) color: {}, d: {}, π: {}'.format(v.id,v.color,v.d,v.π.id if v.π != None else v.π))

    def deepSearch(self):
        for u in self.vertices.values():
            u.color = 'white'
            u.π = None
        self.time = 0
        for v in self.vertices.values():
            if v.color == 'white':
                self.__deepSearch(v)
        self.__printDeepSearch()

    def __deepSearch(self,u):
        self.time += 1
        u.d = self.time
        u.color = 'gray'
        for key in self.getAdjacents(u.id):
            v = self.vertices[key[0] if self.weighted else key]
            if v.color == 'white':
                self.__deepSearch(v)
        u.color = 'black'
        self.time += 1
        u.f = self.time

    def __printDeepSearch(self):
        print('Deep Search:')
        for v in self.vertices.values():
            print('({}) color: {}, d: {}, f: {}'.format(v.id,v.color,v.d,v.f))
        

'''
    DEBBUGGER
'''
print('Graph Undirected Without Weighted')
print(' (r)-(s) (t)-(u)\n',
       ' |   | / | / |\n',
       '(v) (w)-(x)-(y)\n')
graph = Graph([('v','r'),('r','s'),('s','w'),('w','t'),('w','x'),('t','u'),('x','u'),('x','y'),('y','u')])
print(graph)
graph.widthSearch('s')
print('-' * 50)

print('Graph Undirected Weighted')
print(' (r)-4-(s)   (t)-1-(u)\n',
       ' |     |   / |   / |\n',
       ' 2     3  6  4  3  4\n',
       ' |     | /   | /   |\n',
       '(v)   (w)-2-(x)-2-(y)\n')
graph = Graph([('v','r',2),('r','s',4),('s','w',3),('w','t',6),('w','x',2),('t','u',1),('x','u',3),('x','y',2),('y','u',4)], True)
print(graph)
print('-' * 50)

print('Graph Directed Without Weighted')
print(' (u)→(v) (w)\n',
       ' ↑   ↓ ↙ ↓ \n',
       '(x) (y)←(z)\n',
       '         ↺')
graph = Graph([('u','v'),('x','u'),('v','y'),('y','x'),('w','y'),('w','z'),('z','y'),('z','z')], False, True)
print(graph)
graph.deepSearch()
print('-' * 50)

print('Graph Directed Weighted')
print(' (u)-4→(v)  (w)\n',
       ' ↑     |   / | \n',
       ' 2     3  2  3  \n',
       ' |     ↓↙    ↓ \n',
       '(x)←3-(y)←2-(z)\n',
       '             ↺0')
graph = Graph([('u','v',4),('x','u',2),('v','y',3),('y','x',3),('w','y',2),('w','z',3),('z','y',2),('z','z',0)], True, True)
print(graph)
graph.deepSearch()
print('-' * 50)
