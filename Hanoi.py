'''
        Project: Torre de Hanói
        Description: Solução recursiva da Torre de Hanói com o menor número de movimentos
'''
def hanoi(num, orig=[], aux=[], dest=[], result=[]):
    ''' Solução recursiva da Torre de Hanói '''
    #Inicialização
    if len(orig) == len(aux) == len(dest) == 0:
        for i in range(1, num + 1):
            orig.append(i)
        result = [1, orig, dest, aux, num]
        #Impressão de caso inicial
        print('\nInicio')
        for i in range(3):
            print(('Torre%i' % (i + 1)) + ':', result[i + 1])
    #Solução
    if(num > 0):
        #Recursão origem-auxiliar
        hanoi(num - 1, orig, dest, aux, result)
        #Mover disco
        orig.sort()
        aux.append(orig.pop(0))
        aux.sort()
        #Impressão passo a passo
        print(('\nPasso ' + str(result[0])))
        for i in range(3):
            print(('Torre%i' % (i + 1)) + ':', result[i + 1])
        if result[0] == 2 ** result[4] - 1:
            print('\nFim. Total', result[0], 'movimentos')
        result[0] += 1
        #Recursão auxiliar-destino
        hanoi(num - 1, dest, aux, orig, result)

def inputValidInt(label):
    ''' Retorna um inteiro válido digitado pelo usuário '''
    try:
        num = int(float(input(label)))
    except:
        print('Erro: a entrada precisa ser um inteiro.')
        return inputValidInt(label)
    return num

def main():
    ''' Função Inicial '''
    print('----------- TORRE DE HANÓI  ----------')
    disks = inputValidInt('Digite o número de discos: ')
    hanoi(disks)

main()
