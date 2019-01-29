'''
        Project: Número Primo
        Description: Retorna se o número parametro é primo
        Name: Júlio César de Carvalho Barros
        Email: jccb2@cin.ufpe.br
'''
num = int(input("Digite um número inteiro positivo: "))

def isPrime(num):
    ''' Retorna o resultado booleano da verificação de número primo'''
    prime = True if num > 2 else False
    count = 2
    while(count <= int(num ** 0.5) and prime):
        if(num % count == 0):
            prime = False
        count += 1
    return prime

print(isPrime(num))
