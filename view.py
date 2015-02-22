#Autores: Andre Coradin Gulin e Fernando P. Domingues.
#Arquivo de apresentacao de conteudo
#Colocar neste arquivo apenas codigos de coisas
#que serao aprentadas na tela ou codigos de tratamento das mesmas

def welcome_text():                                                             #Alterar esta parada conforme surgir mais funcoes
    print "#=======================================================#"           #Tentar manter em ordem alfabetica, tentar...
    print "#                     GAMBIFACIL                        #"           #E sim, eh apenas uma funcao para mostrar coisas de tela inicial...
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

def get_options_interface():                                                    #Sim, soh para pegar o q o infeliz digita
    return raw_input().lower()

def feedback_messages(num_msg):                                                 #Deixar todas as msgs do programa aqui, mas facil de rastrear e alterar, acho...
    if num_msg == 1:
        print "Baixando zip de facilidades..."
    elif num_msg == 2:
        print "Terminei de baixar facilidades, olhe a pasta local."
    elif num_msg == 3:
        print "Extraindo facilidades..."
    elif num_msg == 4:
        print "Terminei de extrair facilidades."
    else:
        print "MODAFOCA"
