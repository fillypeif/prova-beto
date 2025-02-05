"""
Exercício 2 – Agrupando Argumentos por Tipo

Objetivo:
Crie uma função chamada `separar_tipos` que receba um número arbitrário de argumentos posicionais e retorne um dicionário com duas chaves:
    - 'numeros': contendo uma lista com todos os argumentos que são do tipo int ou float;
    - 'strings': contendo uma lista com todos os argumentos que são do tipo str.
    
Observação:
- Argumentos de outros tipos devem ser ignorados.

Exemplo de chamada:
    resultado = separar_tipos(10, 'Python', 3.14, True, 'Teste', 42)
    print(resultado)
    # Saída esperada: {'numeros': [10, 3.14, 42], 'strings': ['Python', 'Teste']}
    
Requisitos:
- Use estruturas condicionais e funções built-in (como isinstance) para classificar os argumentos.
"""
# Sua solução aqui

def separar_tipos(*args):
    '''
    Separa os tipos de cada valor, str, float, int...
    '''
    numeros = []
    strings = []
    for arg in args:
        if isinstance(arg, int):
            numeros.append(arg)
        elif isinstance(arg, float):
            numeros.append(arg)
        elif isinstance(arg, str):
            strings.append(arg)

    return {'numeros': numeros, 'strings': strings}

print(separar_tipos(1, 2.3, 'so'))
# print('welcome')