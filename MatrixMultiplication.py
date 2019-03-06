'''
        Project: Multiplicação de Matrizes
        Description: Retorna o produto de duas matrizes
        Name: Júlio César de Carvalho Barros
        Email: jccb2@cin.ufpe.br
'''
def matrixMultiplication(a=[], b=[]):
    #Obtendo tamanhos
    lenRowA = len(a)
    lenRowB = len(b) if (len(a) == len(b[0])) else 0
    lenColB = len(b[0])
    #Declarando matriz resultante
    c = []
    #Percorrendo linhas de A
    for rowA in range(lenRowA):
        rowC = []
        #Percorrendo colunas de B
        for colB in range(lenColB):
            #Variável auxiliar para evitar a repetição nas outras linha
            aux = 0
            #Percorrendo linhas de B
            for rowB in range(lenRowB):
                #Somando o produto a mariz
                aux += a[rowA][rowB] * b[rowB][colB]
            #Adiciona o valor a cada linha
            rowC.append(aux)
        #Adicionando cada linha a matriz resultante
        c.append(rowC)
    return c

def main():
    ''' Função Inicial '''
    print('----- MULTIPLICAÇÃO DE MATRIZES  -----')
    #Declarando as matrizes iniciais
    a = [[2,3],[0,1],[-1,4]]
    b = [[1,2,3],[-2,0,4]]
    print('A =',a)
    print('B =',b)
    print('A * B =', matrixMultiplication(a,b))
    print('B * A =', matrixMultiplication(b,a))
    '''
    #Resultado esperado:
    A * B = [[-4,4,18],[-2,0,4],[-9,-2,13]]
    B * A = [[-1,17],[-8,10]]
    '''

main()