#Autores: Andre Coradin Gulin e Fernando P. Domingues.
#Arquivo de estatisticas, ou seja, muita magia negra de contagem estara aqui
#se ocorrer algum outro tipo de magia nesse arquivo, seremos amaldicoados a
#nunca ganhar porras, entao separe esta caceta

import view as v
import data as d

golden_ratio = (1 + 5 ** 0.5) / 4                           #dividi a proporcao aurea por 2 
meuRandom = 1


def count_numbers(mat):                          #funcao que conta a ocorrencia de cada numero e retorna um vetor com esses valores
    vet = [0]*26                                 #o espaco alocado para o indice zero eh perdido, mas escolhi isso a ter q 
    for game in mat:                             #q ficar fazendo somas em todos os for's
         for number in game:                     #uso o numero do sorteio como indice do vetor de contagem
            vet[number] +=1
    return vet

def count_pairs(mat):
    mat_res = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]*26
    vet_temp = [0]*26
    for number1 in range(1,26):
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
    for x in mat:
        for y in x:
            print " {0:3d}".format(y),
        print ""
    print ""
    return mat

def find_path(mat, node_start, len_path, vet_occur):
    path = []
    gtfo = 1

    global meuRandom
    global golden_ratio
    meuRandom = float(d.get_random()) * golden_ratio # calcula prop. aurea * random  uma soh vez para reduzir custos.

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
        #print 'Tamanho do caminho: '+str(len(path)) # quase desnecessario agora
    v.msgs("MSG_CAMINHANDO_END")
    return sorted(path)

# do jeito que estava antes
def heuristic_1_bak(vet_occur, neighborhood_node):
    temp = [0.0]*26
    index = 0
    golden_ratio = (1 + 5 ** 0.5) / 4                           #dividi a proporcao aurea por 2 
    for neighbor in neighborhood_node:
        temp[index] = float(neighbor) * float(vet_occur[index]) * float(d.get_random()) * golden_ratio
        index +=1
    return neighborhood_node.index(max(neighborhood_node))

# versao modafocamente mais rapida
def heuristic_1(vet_occur, neighborhood_node):
    global meuRandom
    temp = [0.0]*26
    index = 0
    for neighbor in neighborhood_node:
        temp[index] = float(neighbor) * float(vet_occur[index]) * meuRandom # * golden_ratio  #aurea*random jah calculado
        index += 1
    return neighborhood_node.index(max(neighborhood_node))




# calc a qntos jogos que cada numero sai ou nao
# Aumenta ou diminui a "probabilidade" do numero na matriz de pares, baseado em observacoes 
def calcSeqLast(mat_jogos, mat_pairs): #TODO: nome temporario fei bagarai....
    MAX = 10.0                                             # Defini como 10 o maximo de jogos consecutivos que numero sai, com base em observacoes
    MAX2 = 5.0                                             # 5 como maximo de jogos que numero passa sem sair.
    cont = [0]*26
    k = 0.0

    j = len(mat_jogos)-1                                   # indice do ultimo jogo.
    for i in range(1,26):                                  # calculo a quanto tempo um numero tem ou nao saido
        c = 1
        k=0.0
        if i in mat_jogos[j]:                              # se o numero saiu no ultimo jogo calculo a quantos jogos ele tem saido
            while i in mat_jogos[j-c]:
                c += 1                                     # c == numero de jogos que numero sai.
            if c > 1:
                #if c > MAX: # como estou fazendo uma divisao pelo dobro do maior numero de sequencias jah visto,
                    #c = MAX # limitar o numero 'c' nao tem relevancia...
                k = 1 - c/(MAX*2)                          # mantem k entre 0,5 e 1. quanto mais tempo o numero sai, menor a chance de sair novamente.
                for l in xrange(i+1, 26):
                    mat_pairs[i][l] = int(mat_pairs[i][l] * k)
        else:                                              # * Se o numero NAO saiu, calculo a quantos jogos ele NAO sai.
            while i not in mat_jogos[j-c]:                 # * Basicamente o inverso da parte acima.
                c += 1
            if c > 1: # k==1 mantem tudo igual. 
                #if c > MAX2:
                    #c = MAX2
                k = 1 + c/(MAX2*2)                         # mantem k entre 1 e 1,5. quanto mais tempo numero nao sai, maior a chance de sair.
                for l in xrange(i+1, 26):
                    mat_pairs[i][l] = int(mat_pairs[i][l] * k)

    load_graph(mat_pairs)
#fim dessa loucura
#\calcSeqLast
