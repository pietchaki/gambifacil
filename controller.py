#Autores: Andre Coradin Gulin e Fernando P. Domingues.
#Arquivo juncao da porra toda
#Colocar neste arquivo apenas codigos para chamar as
#coisas tudo (apresentacao, recupera dados, estatistica e probabilidade)
#Definir aqui tbm o padrao de coding, pq senao vai ficar uma salada
#1 - nome de funcao, variavel e o caralho a quarta em ingles e q se foda modafoca
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
import data as d
import statistics as s
import probability as p

#=====================================================================#
#parte de variaveis globais
global mat_jogos
global mat_aposta
#=====================================================================#
#parte das outras paradas

def main():

    mat_results = []
    vet_occur = []
    mat_occur_pairs = []

    v.msgs("MSG_WELCOME")
    v.msgs("MSG_OPTIONS")

    mat_jogos = d.get_numbers()

    v.msgs("MSG_>")

    option_user = v.get_options_interface()

    while option_user != "s":
        if option_user  == "a":
            d.get_zipfile()
            d.unzip('./D_lotfac.zip','.')
        if option_user  == "b":
            mat_jogos = d.get_numbers()
        elif option_user  == "c":
            vet_occur = s.count_numbers(mat_jogos)
            print vet_occur
            v.msgs("MSG_UHULL")
        elif option_user  == "g":
            mat_occur_pairs = s.count_pairs(mat_jogos)
            mat_occur_pairs = s.load_graph(mat_occur_pairs)
        elif option_user  == "f":
             print s.find_path(mat_occur_pairs, 1, 15, vet_occur)
        elif option_user  == "l":
            print d.get_lucky()
        elif option_user  == "k":
            print s.calcSeqLast(mat_jogos, mat_occur_pairs)
        elif option_user  == "p":
            v.msgs("MSG_")
        elif option_user  == "h":
            v.msgs("MSG_OPTIONS")
        else:
            v.msgs("MSG_DEU_RUIM")
        v.msgs("MSG_>")
        option_user = v.get_options_interface()
    v.msgs("MSG_END")
if __name__ == "__main__":
    main()
