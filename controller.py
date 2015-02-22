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
import data as d
import statistics as s
import probability as p

#=====================================================================#
#parte de variaveis globais

#=====================================================================#
#parte das outras paradas

def main():
    mat_results = []
    v.welcome_text()
    option_user = v.get_options_interface()
    while option_user != "s":
        if option_user  == "b":
            d.get_zipfile()
            d.unzip('./D_lotfac.zip','.')
            mat_results = d.get_numbers()
        elif option_user  == "c":
            v.feedback_messages(0)
        elif option_user  == "g":
            v.feedback_messages(0)
        elif option_user  == "p":
            v.feedback_messages(0)
        else:
            v.feedback_messages(0)
        option_user = v.get_options_interface()   
if __name__ == "__main__":
    main()
