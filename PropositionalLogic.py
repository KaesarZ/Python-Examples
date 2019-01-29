'''
        Project: Lógica Proposicional
        Description: Calcula o valor lógico de uma proposição
'''
def replaceString(string, old_word, new_word):
    ''' Retorna a string com as palavras parâmetros substituídas '''
    string_size = len(string)
    old_size = len(old_word)
    result = str()
    i = 0
    while i < string_size:
        if string[i] == old_word[0]:
            found = True
            j = 0
            while j < old_size and i + j < string_size and found:
                if string[i + j] != old_word[j]:
                    found = False
                j += 1
            if found:
                i += old_size - 1
                result += new_word
            else:
                result += string[i]
        else:
            result += string[i]
        i += 1
    return result

def main(action):
    ''' Função principal  '''
    print('A sentença deve ser composta exclusivamente de: ')
    print('- Variáveis proposicionais (ex: p, q, r, s)')
    print('- Operadores lógicos (ex: ¬, ∨, ∧, →, ↔)')
    print('- Parênteses (ex: "(", ")" )')
    print('- Exemplo: (a∧b), (a→(c∨b)), (¬((¬d)↔(a→c)))\n')
    sentence = input('Digite a sentença: ')
    #Tratando sentença
    result = str()
    var_props = []
    for char in sentence:
        var = char.lower()
        if (char in ['T','F','(','¬', '∨', '∧', '→', '↔',')']):
            result += char
        elif (var >= 'a' and var <= 'z'):
            if var not in var_props:
                var_props.append(var)
            result += var
    sentence = result
    #Obter valor das variáveis propsicionais
    print('\nAtribua os valores lógicos as variáveis proposicionais:')
    values = {'T':'T', 'F':'F'}
    for var in range(len(var_props)):
        val = input(str(var_props[var]) + ' (T/F): ').upper()
        while val != 'T' and val != 'F':
            print('Erro: o valor precisa ser "T" para True ou "F" para False.')
            val = input(str(var_props[var]) + ' (T/F): ').upper()
        values[var_props[var]] = val
    #Substituir valores pela tabela
    for key in values.keys():
        result = replaceString(result, key, values[key])
    #Resolução e impressão passo a passo
    print('\n' + sentence)
    while len(result) > 1:
        for key in table.keys():
            if key in result:
                result = replaceString(result, key, table[key])
                print('≡', result)
    print('\nEsta sentença é:', True if result == 'T' else False)
        
#Constante
table = {
    #Base
    '(T)':'T',
    '(F)':'F',
    #Negação
    '(¬T)':'F',
    '(¬F)':'T',
    #Ou
    '(T∨T)':'T',
    '(T∨F)':'T',
    '(F∨T)':'T',
    '(F∨F)':'F',
    #E
    '(T∧T)':'T',
    '(T∧F)':'F',
    '(F∧T)':'F',
    '(F∧F)':'F',
    #Implicação
    '(T→T)':'T',
    '(T→F)':'T',
    '(F→T)':'F',
    '(F→F)':'T',
    #Se-somente-se
    '(T↔T)':'T',
    '(T↔F)':'F',
    '(F↔T)':'F',
    '(F↔F)':'T',
}
#Inicialização
main(table)
