#Autores: Andre Coradin Gulin e Fernando P. Domingues.
#Arquivo de estatisticas, ou seja, muita magia negra de contagem estara aqui
#se ocorrer algum outro tipo de magia nesse arquivo, seremos amaldicoados a
#nunca ganhar porras, entao separe esta caceta

import view as v
import data as d

def count_numbers(mat):                          #funcao que conta a ocorrencia de cada numero e retorna um vetor com esses valores
    vet = [0]*26                                 #o espaco alocado para o indice zero eh perdido, mas escolhi isso a ter q 
    for game in mat:                             #q ficar fazendo somas em todos os for's
         for number in game:                     #uso o numero do sorteio como indice do vetor de contagem
            vet[number] +=1
    return vet

def count_pairs(mat):
    mat_res = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]*26
    vet_temp = [0]*26
    for number1 in range(1,25):
        for number2 in range(number1+1,26):
            for game in mat:
                if (number1 in game) and (number2 in game):
                    vet_temp[number2]+=1
        mat_res[number1] = vet_temp[:]
        vet_temp = [0]*26
    return mat_res

def init_graph():
     return [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]*25  #ao inves de usar uma biblioteca vou fazer na mao
                                                                        # o grafo sera uma lista de listas
                                                                        #cada lista indica um nodo, por consequencia um numero sorteado
                                                                        #cada numero dessa lista, indica a interacao daquele numero sorteado com o numero sorteado do index
                                                                        #ex: na segunda lista no terceiro valor esta indicado quantas vezes o numero dois saiu com o numero tres
def load_graph(mat):
    index = 1
    index2 = 1
    v.msgs("MSG_GRAFANDO")
    while (index < 26):
        while (index2 < 26):
            mat[index2][index] = mat[index][index2]
            index2+=1
        index+=1
        index2=index
    v.msgs("MSG_GRAFANDO_END")        
    return mat

def find_path(mat, node_start, len_path, vet_occur):
    path = []
    gtfo = 1
    v.msgs("MSG_CAMINHANDO")
    while len(path) < len_path:
        neighborhood = mat[node_start]
        while gtfo:
             #next_node =  neighborhood.index(max(neighborhood))
             next_node = heuristic_1(vet_occur,neighborhood)
             if next_node not in path:
                 path.append(next_node)
                 gtfo = 0
             else:
                 neighborhood.pop(next_node)
        gtfo = 1
        node_start = next_node
        print 'Tamanho do caminho: '+str(len(path))
    v.msgs("MSG_CAMINHANDO_END")
    return sorted(path)

def heuristic_1(vet_occur, neighborhood_node):
    temp = [0.0]*26
    index = 0
    golden_ratio = (1 + 5 ** 0.5) / 4                           #dividi a proporcao aurea por 2 
    for neighbor in neighborhood_node:
        temp[index] = float(neighbor) * float(vet_occur[index]) * float(d.get_random()) * golden_ratio
        index +=1
    return neighborhood_node.index(max(neighborhood_node))
        
