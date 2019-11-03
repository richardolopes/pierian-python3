'''
    Aula 11
'''
a = "Python 3"
print(len(a)) # 8

# Retorna toda a string
# VAR:VAR - Retorna uma parte da string
# ::VAR - Retorna uma parte da string, sendo ":" o começo da string
# ::-1 - Retorna a string ao contrário
print(a[:]) # Python 3
print(a[1:4]) # yth
print(a[::2]) # Pto
print(a[::-1]) # 3 nohtyP

a = "Python "
print(a * 10) # Python Python Python Python Python Python Python Python Python Python 

# Strings são imutáveis
print(a.lower()) # python

a = "A computação quântica é a ciência que estuda as aplicações das teorias e propriedades da mecânica quântica na Ciência da Computação."
print(a.split()) # ['A', 'computação', 'quântica', 'é', 'a', 'ciência', 'que', 'estuda', 'as', 'aplicações', 'das', 'teorias', 'e', 'propriedades', 'da', 'mecânica', 'quântica', 'na', 'Ciência', 'da', 'Computação.']

print(a.split("o")) # ['A c', 'mputaçã', ' quântica é a ciência que estuda as aplicações das te', 'rias e pr', 'priedades da mecânica quântica na Ciência da C', 'mputaçã', '.']


'''
    Aula 13 - Formatações de impressões
'''
var = 'R'
# %s = str()
# %r = repr()
print("Olá %s, tudo bem? %s?" %(var, var)) # Olá R, tudo bem? R?
print("Olá " + var + ", tudo bem?") # Olá R, tudo bem?
print("Pontos flutuantes: %11.5f" %(23.344)) # Pontos flutuantes:    23.34400
print("O preço de um iPhone X é %d" %(5559.99)) # O preço de um iPhone X é 5559
print("Olá {}, tudo bem?" .format("Richard")) # Olá Richard, tudo bem?
print("O preço de um celular com suporte a 4 chips e um som mais alto que de uma JBL é {}" .format(123.5)) # O preço de um celular com suporte a 4 chips e um som mais alto que de uma JBL é 123.5
print("Um: {a}, dois: {b}, três: {c}".format(a = 1, b = "dois", c = 3.5)) # Um: 1, dois: dois, três: 3.5


'''
    Aula 15 - Manipulação de listas
'''
lista = ["ZERO", "UM", "DOIS"]
lista += ["TRÊS"]
print(lista) # ['ZERO', 'UM', 'DOIS', 'TRÊS']

print(type(lista)) # list

print(len(lista)) # 4

lista.append("QUATRO") # ['ZERO', 'UM', 'DOIS', 'TRÊS', 'QUATRO']
print(lista.pop()) # 'QUATRO'

tres = lista.pop(3)
print(tres) # TRÊS

lista.reverse()
print(lista) # ['DOIS', 'UM', 'ZERO']

lista = [5, 7, 9, 1, 6, 0, 23, 51]
lista.sort()
print(lista) # [0, 1, 5, 6, 7, 9, 23, 51]

lista = ["b", "d", "z", "x", "a", "r"]
lista.sort()
print(lista) # ['a', 'b', 'd', 'r', 'x', 'z']

lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
lista3 = [7, 8, 9]

matrix = [lista1, lista2, lista3]
print(matrix) # [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

primeira_coluna = [row[0] for row in matrix]
print(primeira_coluna) # [1, 4, 7]


'''
    Aula 17 - Dicionários
'''
dic = {
    "Nome": "Richard",
    "Idade": 18,
    "Cachorros": [
            {
                "Nome": "Mel",
                "Idade": 5
            },
            {
                "Nome": "Lessie",
                "Idade": 12
            }
        ]
    }

print(dic["Cachorros"][0]["Nome"]) # Mel

print( list(dic.keys()) ) # ['Nome', 'Idade', 'Cachorros']

print( list(dic.items()) ) # [('Nome', 'Richard'), ('Idade', 18), ('Cachorros', [{'Nome': 'Mel', 'Idade': 5}, {'Nome': 'Lessie', 'Idade': 12}])]


'''
    Aula 19 - Tuplas
'''
t = ("zero", 1, 2, "três")

print(type(t)) # tuple

# Tuplas são imutáveis.
# t[0] = 0 # Erro


'''
    Aula 20 - Arquivos
'''
arq = open("section-03.txt")
print(arq) # <_io.TextIOWrapper name='section-03.txt' mode='r' encoding='cp1252'>
print(arq.read()) 
# Arquivo de texto.
# Arquivo de texto2.
# Arquivo de texto3.

print(arq.seek(0)) # 0
print(arq.readline()) # Arquivo de texto.

print("----")

arq.seek(0)
for line in arq:
    print(line)

# Arquivo de texto.
#
# Arquivo de texto2.
#
# Arquivo de texto3.


'''
    Aula 21 - Sets e Booleanos
'''
a = set()
a.add(1)
print(a) # {1}

a.add(2)
a.add(3)
a.add(1)
print(a) # {1, 2, 3}

a = set([1,1,2,3])
print(a) # {1, 2, 3}

a = True
b = False