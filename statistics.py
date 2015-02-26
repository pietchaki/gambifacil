#Autores: Andre Coradin Gulin e Fernando P. Domingues.
#Arquivo de estatisticas, ou seja, muita magia negra de contagem estara aqui
#se ocorrer algum outro tipo de magia nesse arquivo, seremos amaldicoados a
#nunca ganhar porras, entao separe esta caceta


def count_numbers(mat):                          #funcao que conta a ocorrencia de cada numero e retorna um vetor com esses valores
    vet = [0]*26                                 #o espaco alocado para o indice zero eh perdido, mas escolhi isso a ter q 
    for game in mat:                             #q ficar fazendo somas em todos os for's
         for number in game:                     #uso o numero do sorteio como indice do vetor de contagem
            vet[number] +=1
    return vet
