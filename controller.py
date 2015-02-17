#Autores: Andre Coradin Gulin e Fernando P. Domingues.
#Arquivo juncao da porra toda
#Colocar neste arquivo apenas codigos para chamar as
#coisas tudo (apresentacao, recupera dados, estatistica e probabilidade)
#Definir aqui tbm o padrao de coding, pq senao vai ficar uma salada
#1 - nome de funcao, variavel o  caralho a quarta
#em ingles e q se foda modafoca
#2 - definir variaveis globais aqui e agora
#3 - padrao de tab = 4 espacos, pq eh bonito
#4 - nada de acento nesta caceta
#5 - comentar toda santa funcao, pq nem Odin sabe oq essas porra fazem
#6 - Usar post-rock para codar #ficadica

#=====================================================================#
#parte de imports

import view as v
import dates as d
import statistics as s
import probability as p
import getopt as go

#=====================================================================#
#parte de variaveis globais

#=====================================================================#
#parte das outras paradas

def main():
    # pega os comandos passados pela chamada do programis
    try:
        opts, args = go.getopt(sys.argv[1:], "h", ["help"])
    except getopt.error, msg:
        print msg
        print "for help use --help"
        sys.exit(2)
    # process options
    for o, a in opts:
        if o in ("-h", "--help"):
            print __doc__
            sys.exit(0)
    # process arguments
    for arg in args:
        process(arg) # process() is defined elsewhere

if __name__ == "__main__":
    main()
