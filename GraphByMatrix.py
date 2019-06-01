'''
        Project: Graph
        Description: Implementation by matrix
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
        self.matrix = []
        self.vertices = []
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
        result = 'Matrix of Adjacency\n   '
        for vertice in self.vertices:
            result += '{:^3}'.format(vertice.id)
        result += '\n'
        for i in range(len(self.vertices)):
            result += '{}: {}\n'.format(self.vertices[i].id,self.matrix[i])
        return result

    def __repr__(self):
        result = 'Matrix of Adjacency\n   '
        for vertice in self.vertices:
            result += '{:^3}'.format(vertice.id)
        result += '\n'
        for i in range(len(self.vertices)):
            result += '{}: {}\n'.format(self.vertices[i].id,self.matrix[i])
        return result
    
    def addVertice(self,id):
        vertice = Vertice(id)
        if not vertice in self.vertices: 
            self.matrix.append([0] * len(self.vertices))
            self.vertices.append(vertice)
            for v in self.matrix:
                v.append(0)

    def addEdge(self,origin,destiny,weight=None):
        i = self.vertices.index(origin)
        j = self.vertices.index(destiny)
        weight = 1 if not self.weighted else weight
        self.matrix[i][j] = weight
        if not self.directed:
            self.matrix[j][i] = weight
    
    def remVertice(self,id):
        vertice = Vertice(id)
        if vertice in self.vertices:
            i = self.vertices.index(vertice)
            del self.vertices[i]
            del self.matrix[i]
            for v in self.matrix:
                del v[i]
        else:
            raise KeyError
    
    def remEdge(self,origin,destiny,weight=None):
        origin = Vertice(origin)
        destiny = Vertice(destiny)
        o = self.vertices.index(origin)
        d = self.vertices.index(destiny)
        if origin in self.vertices and destiny in self.vertices:
            found = True
            self.matrix[o][d] = 0
            if not self.directed:
                    self.matrix[d][o] = 0
        else:
            raise KeyError

    def isLinked(self,id1,id2):
        i = self.vertices.index(id1)
        j = self.vertices.index(id2)
        return (self.matrix[i][j] != 0)

    def getInputDegree(self,id):
        vertice = Vertice(id)
        count = 0
        i = self.vertices.index(vertice)
        for vertice in self.matrix:
            if vertice[i] != 0:
                count += 1
        return count

    def getOutputDegree(self,id):
        vertice = Vertice(id)
        count = 0
        i = self.vertices.index(vertice)
        for edge in self.matrix[i]:
            if edge != 0:
                count += 1
        return count

    def getDegree(self,vertice):
        if self.directed:
            return self.getInputDegree(vertice) + self.getOutputDegree(vertice)
        else:
            return self.getOutputDegree(vertice)

    def getAdjacents(self,vertice):
        i = self.vertices.index(vertice)
        adjacents = []
        j = 0
        for j in range(len(self.vertices)):
            if self.matrix[i][j] != 0:
                adjacents.append(self.vertices[j])
        return adjacents
    
    def getSmallerEdge(self):
        weight = float('inf')
        smallers = []
        if self.weighted:
            i = 0
            j = 0
            for i in range(len(self.matrix)):
                for j in range(len(self.matrix[i])):
                    if self.matrix[i][j] != 0 and self.matrix[i][j] == weight:
                        smallers.append(Edge(self.vertices[i],self.vertices[j],self.matrix[i][j]))
                    elif self.matrix[i][j] != 0 and self.matrix[i][j] < weight:
                        weight = self.matrix[i][j]
                        smallers = [Edge(self.vertices[i],self.vertices[j],self.matrix[i][j])]
            return smallers
        
    def getHigherEdge(self):
        weight = 0
        highers = []
        if self.weighted:
            i = 0
            j = 0
            for i in range(len(self.matrix)):
                for j in range(len(self.matrix[i])):
                    if self.matrix[i][j] != 0 and self.matrix[i][j] == weight:
                        highers.append(Edge(self.vertices[i],self.vertices[j],self.matrix[i][j]))
                    elif self.matrix[i][j] != 0 and self.matrix[i][j] > weight:
                        weight = self.matrix[i][j]
                        highers = [Edge(self.vertices[i],self.vertices[j],self.matrix[i][j])]
            return highers

    def widthSearch(self,id):
        for v in self.vertices:
            v.color = 'white'
            v.d = float('inf')
            v.π = None
        s = self.vertices[self.vertices.index(Vertice(id))]
        s.color = 'gray'
        s.d = 0
        s.π = None
        Q = [s]
        while len(Q) > 0:
            u = Q.pop(0)
            for v in self.getAdjacents(u.id):
                if v.color == 'white':
                    v.color = 'gray'
                    v.d = u.d + 1
                    v.π = u
                    Q.append(v)
            u.color = 'black'
        self.__printWidthSearch()

    def __printWidthSearch(self):
        print('Width Search:')
        for v in self.vertices:
            print('({}) color: {}, d: {}, π: {}'.format(v.id,v.color,v.d,v.π.id if v.π != None else v.π))

    def deepSearch(self):
        for u in self.vertices:
            u.color = 'white'
            u.π = None
        self.time = 0
        for v in self.vertices:
            if v.color == 'white':
                self.__deepSearch(v)
        self.__printDeepSearch()

    def __deepSearch(self,u):
        self.time += 1
        u.d = self.time
        u.color = 'gray'
        for v in self.getAdjacents(u.id):
            if v.color == 'white':
                self.__deepSearch(v)
        u.color = 'black'
        self.time += 1
        u.f = self.time

    def __printDeepSearch(self):
        print('Deep Search:')
        for v in self.vertices:
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
