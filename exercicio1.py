"""
Exercício 1 – Identificando Quadrados Perfeitos

Objetivo:
Crie uma função chamada `classificar_quadrados` que receba uma lista de números inteiros e retorne um dicionário com duas chaves:
    - 'quadrados_perfeitos': contendo os números que são quadrados perfeitos (por exemplo, 1, 4, 9, 16, …);
    - 'nao_quadrados': contendo os demais números.

Requisitos:
- Utilize laços de repetição para percorrer a lista.
- Adicione uma docstring explicando o funcionamento da função.

Exemplo de chamada:
    resultado = classificar_quadrados([1, 2, 3, 4, 8, 9, 15])
    print(resultado)
    # Saída esperada: {'quadrados_perfeitos': [1, 4, 9], 'nao_quadrados': [2, 3, 8, 15]}
    
Importante:
- Não se preocupe com números negativos.
"""
# Sua solução aqui

from math import pi

arr = [1, 2, 3, 4, 8, 9, 15]

def classificar_quadrados(array):
    '''
    Classica os quadrados como nao quadrados e quadrados perfeitos 
    '''
    dic = {}
    quadrados_perfeitos = []
    nao_quadrados = []
    for x in array:
        if x % 2 == 0:
            quadrados_perfeitos.append(x)
        else:
            nao_quadrados.append(x)

    dic['nao_quadrados'] = nao_quadrados
    dic['quadrados_perfeitos'] = quadrados_perfeitos

    return {'quadrados_perfeitos': dic['quadrados_perfeitos'], 'nao_quadrados': dic['nao_quadrados']}

# professor, fiz essa gambiarra pq deu um branco total, acredito que tenha forma melhor. Mas essa foi a melhor que consegui. 
print(classificar_quadrados(arr))