"""
Exercício 3 – Processamento de Nomes com Tuplas

Objetivo:
1. Solicite ao usuário uma entrada contendo uma sequência de nomes separados por vírgula.
2. Converta essa entrada em uma lista de strings, garantindo a remoção de espaços desnecessários e a conversão para minúsculas.
3. Crie uma função chamada `nome_e_tamanho` que receba um nome (string) e retorne uma tupla contendo:
    - O próprio nome.
    - O tamanho (número de caracteres) do nome.
4. Utilize essa função para transformar cada nome da lista em uma tupla (nome, tamanho) e armazene essas tuplas em uma nova lista.
5. Percorra a nova lista e, para cada tupla, imprima uma mensagem informando se o nome possui mais de 5 caracteres ou não.

Exemplo de mensagem:
    "O nome 'Carlos' tem 6 caracteres e é considerado longo." 
    ou 
    "O nome 'Ana' tem 3 caracteres e é considerado curto."

Requisitos:
- Faça uso de laços de repetição e estruturas condicionais.
- Garanta o tratamento adequado da entrada do usuário.
"""
# Sua solução aqui


def nome_e_tamanho(string):
    counter = 0
    nomes = string.lower().split(',')
    obj = {}

    for nome in nomes:
        if len(nome) >= 5: #big
            obj[nome] = len(nome)
        else:
            obj[nome] = len(nome)

    return obj

array_nomes = nome_e_tamanho('ANA, JOAO, CARLOS, LUSCASVINICIUS')

def lista(arr):
    obj235 = []
    for nome, tamanho in arr.items():
        nome = nome.strip()
        if tamanho >= 5:
            obj235.append({'nome': nome, '__str__': f'O nome de {nome} é grande.'})
        else:
            obj235.append({'nome': nome, '__str__': f'O nome de {nome} é pequeno.'})
    return obj235


lista_var = lista(array_nomes)


def percorrer_lista(lista):
    for i in lista:
        print(i['__str__'])

percorrer_lista(lista_var)