#Autores: Andre Coradin Gulin e Fernando P. Domingues.
#Arquivo de apresentacao de conteudo
#Colocar neste arquivo apenas codigos de coisas
#que serao aprentadas na tela ou codigos de tratamento das mesmas

def welcome_text():                                                             #Alterar esta parada conforme surgir mais funcoes
    print "#=======================================================#"           #Tentar manter em ordem alfabetica, tentar...
    print "#                     GAMBIFACIL                        #"           #E sim, eh apenas uma funcao para mostrar coisas de tela inicial...
    print "# Solucao em facilidades facilitadoras de coisas faceis #"


def get_options_interface():                                                    #Sim, soh para pegar o q o infeliz digita
    return raw_input().lower()

def msgs(msg):                                                 #Deixar todas as msgs do programa aqui, mas facil de rastrear e alterar, acho...
    if   msg == "MSG_>":
        print "> ",
    elif msg == "MSG_DOWN_JOGOS":
        print "Baixando zip de facilidades..."
    elif msg == "MSG_DOWN_JOGOS_END":
        print "Terminei de baixar facilidades, olhe a pasta local."
    elif msg == "MSG_EXTRACT":
        print "Extraindo facilidades..."
    elif msg == "MSG_EXTRACT_END":
        print "Terminei de extrair facilidades."
    elif msg == "MSG_FIND_JOGOS":
        print "Encontrando sequencias de facilidades..."
    elif msg == "MSG_FIND_JOGOS_END":
        print "Terminei de encontrar sequencias faceis"

# ta tudo muito bonito, bora zoar... heheheh
    elif msg == "MSG_END":
        print "\n\tAdeus,\n\t  E obrigado pelos peixes!\n\n"

    elif msg == "MSG_UHULL":
        print "MODAFOCA"
    elif msg == "MSG_DEU_RUIM":
        print "Put a Keep are You... Full Del!"
    elif msg == "MSG_":
        print "Option only available in paid version."

    elif msg == "MSG_OPTIONS":
        print "#=======================================================#"
        print "#                      OPCOES                           #"
        print "# B - Baixar facilidade                                 #"
        print "# C - Contar e gerar arquivo de facilidades             #"
        print "# G - Gerar grafo de facilidade                         #"
        print "# P - Calcular facilidades que ainda nao foram faceis   #"
        print "# S - Sair da facilidade                                #"
        print "#=======================================================#"
    else:
        print "ERROR: Error Message failed to pri",
