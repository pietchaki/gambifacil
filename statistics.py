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

def count_pairs(mat):
    mat_res = [[]]*25
    vet_temp = [0]*26
    for number1 in range(1,25):
        for number2 in range(number1+1,26):
            for game in mat:
                if (number1 in game) and (number2 in game):
                    vet_temp[number2]+=1
        mat_res[number1] = vet_temp[:]
        vet_temp = [0]*26
    return mat_res
        
