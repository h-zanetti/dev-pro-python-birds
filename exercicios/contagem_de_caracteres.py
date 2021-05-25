def contar_caracteres(s):
    '''Função que conta os caracteres de uma string
    EX:
    >>> contar_caracteres("banana")
    {'a': 3, 'b': 1, 'n': 2}
    >>> contar_caracteres("Henrique")
    {'e': 2, 'h': 1, 'i': 1, 'n': 1, 'q': 1, 'r': 1, 'u': 1}

    :parm s: string
    :return: dictionary com chaves sendo as letras e os valores sua contagem
    '''
    resultado = {}

    for caracter in s:
        resultado[caracter] = resultado.get(caracter, 0) + 1

    return resultado

if __name__ == '__main__':
    print(contar_caracteres('banana'))
    print(contar_caracteres('Henrique'))