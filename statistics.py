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
    for x in mat:
        for y in x:
            print " {0:3d}".format(y),
        print ""
    print ""
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
        


#TODO:
#WARNING:
#
# Uma alternativa a esta funcao, seria simplesmete reduzir a probabilidade do numero quando
# o jogo siu recentemente, e aumentar a probabilidade quando o numero nao saiu recentemente.
#
# Algo como, se numero saiu nos ultimos 3 jogos reduzo P*3 da probabilidade (se definirmos P como 5,
# entao reduziriamos 15 pontos) e se numero nao saiu nos ultimos 5 jogos(caso do numero 25 no dia
# que escrevi este comentario), aumentariamos 25 pontos de probabilidade deste numero.
#
# PS.: agora que escrevi os comentarios acima, todas estas funcs abaixo parecem perda de tempo....... mi
#TODO: me de sua opiniao sobre isso e se estes dados na diagonal podem ser uteis em sua func de caminhar no grafo

#calc a qntos jogos que cada numero sai ou nao
def calcSeqLast(mat_jogos, mat_pairs): #TODO: nome temporario fei bagarai....
    MAX = 15                                               # Defini como 15 o maximo de jogos consecutivos que calculo, com base em observacoes
    cont = [0]*26

    j = len(mat_jogos)-1
    for i in range(1,26):                                  # calculo a quanto tempo um numero tem ou nao saido
        k=1
        if i in mat_jogos[j]:                              # se o numero saiu no ultimo jogo calculo a quantos jogos ele tem saido
            while i in mat_jogos[j-k]:
                k+=1                                       # k= numero de jogos que numero sai ou nao.
            k+=1                                           # k+1 => numero de jogos que tera saido se sair novamente... nao sei se isso faz muito sentido
            s=0
            for jogo in mat_jogos:                         # calculo quantas vezes na historia este numero ficou este tanto de tempo saindo ou nao
                if i in jogo:                              # Automagicamente este valor eh maior quando proximo do numero de vezes que mais saiu.
                    s+=1
                else:
                    if s==k:
                        mat_pairs[i][i] += 1               # Insiro este valor na diagonal do grafo
                    s=0
        
        else:                                              # * Se o numero NAO saiu, calculo a quantos jogos ele NAO sai.
            while i not in mat_jogos[j-k]:                 # * Basicamente o inverso da parte acima.
                k+=1
            k+=1
            s=0
            for jogo in mat_jogos:
                if i in jogo:
                    if s==k:
                        mat_pairs[i][i] += 1 #TODO inverter esta probabilidade? no momento ele diz se eh provavel que continue NAO saindo...
                    s=0
                else:
                    s+=1

    for x in mat_pairs:
        for y in x:
            print " {0:3d}".format(y),
        print ""
    print ""
#fim dessa loucura
#\calcSeqLast

#deixarei isto aqui para referencias futuras e caso a ideia acima nao de 'S'erto...
# Calcula quantas vezes cada numero sai em jogos consecutivos.
def calcSeq(mat_jogos):
    MAX = 15                                               # Defini como 10 o maximo de jogos consecutivos que um numero eh sorteado....
    seq = [[0 for x in xrange(MAX+1)]for x in xrange(26)]  # Inicializa vetor de sequencias

    print "# numero de jogos consecutivos em que um numero saiu:"
    for i in range(1,26):
        s=0
        for jogo in mat_jogos:
            if i in jogo:
                s+=1
            else:
                if s>=MAX:
                    seq[i][MAX] += 1
                else:
                    seq[i][s] += 1
                s=0
    #TODO: algo com esses dados

    # Reseta tudo e calcula aos contrarios
    print "\n- - - - - - - - - - - - - - - - - - - - - - - - - - - -\n"
    for i in xrange(26):
        for s in xrange(MAX+1):
            seq[i][s] = 0

    print "# numero de jogos consecutivos em que um numero *NAO* saiu"
    for i in range(1,26):
        s=0
        for jogo in mat_jogos:
            if i in jogo:
                if s>=MAX:
                    seq[i][MAX] += 1
                else:
                    seq[i][s] += 1
                s=0
            else:
                s+=1
    #TODO: algo com esses outros dados