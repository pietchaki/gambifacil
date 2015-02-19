#Autores: Andre Coradin Gulin e Fernando P. Domingues.
#Arquivo juncao da porra toda
#Colocar neste arquivo apenas codigos para chamar as
#coisas tudo (apresentacao, recupera dados, estatistica e probabilidade)
#Definir aqui tbm o padrao de coding, pq senao vai ficar uma salada
#1 - nome de funcao, variavel e o  caralho a quarta
#em ingles e q se foda modafoca
#2 - definir variaveis globais aqui e agora
#3 - padrao de tab = 4 espacos, pq eh bonito
#4 - nada de acento nesta caceta
#5 - comentar toda santa funcao, pq nem Odin sabe oq essas porra fazem
#6 - Usar post-rock para codar #ficadica

#=====================================================================#
#parte de imports

import getopt as go
import sys


import view as v
import dates as d
import statistics as s
import probability as p

#=====================================================================#
#parte de variaveis globais

#=====================================================================#
#parte das outras paradas

def main():
    print "#=======================================================#"
    print "#                     GAMBIFACIL                        #"
    print "# Solucao em facilidades facilitadoras de coisas faceis #"
    print "#  Fodoes: Andre Coradin Gulin e Fernando P. Domingues  #"
    print "#=======================================================#"
    print "#                      OPCOES                           #"
    print "# B - Baixar facilidade                                 #"
    print "# C - Contar e gerar arquivo de facilidades             #"
    print "# G - Gerar grafo de facilidade                         #"
    print "# P - Calcular facilidades que ainda nao foram faceis   #"
    print "# S - Sair da facilidade                                #"
    print "#=======================================================#"
    option_user = raw_input().lower();
    while option_user != "s":
        if option_user  == "b":
            print "B"
        elif option_user  == "c":
            print "C"
        elif option_user  == "g":
            print "G"
        elif option_user  == "p":
            print "P"
        else:
            print "modafoca"
        option_user = raw_input().lower();
if __name__ == "__main__":
    main()
