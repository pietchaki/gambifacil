#Autores: Andre Coradin Gulin e Fernando P. Domingues.
#Arquivo de apresentacao de conteudo
#Colocar neste arquivo apenas codigos de coisas
#que serao aprentadas na tela ou codigos de tratamento das mesmas

class messeges:
    msgs = { "MSG_>":"> ",
             "MSG_DOWN_JOGOS":"Baixando zip de facilidades...",
             "MSG_DOWN_JOGOS_END":"Terminei de baixar facilidades, olhe a pasta local.",
             "MSG_EXTRACT":"Extraindo facilidades...",
             "MSG_EXTRACT_END":"Terminei de extrair facilidades.",
             "MSG_FIND_JOGOS":"Encontrando sequencias de facilidades...",
             "MSG_FIND_JOGOS_END":"Terminei de encontrar sequencias faceis",                        # ta tudo muito bonito, bora zoar... heheheh
             "MSG_END":"\n\tAdeus,\n\t  E obrigado pelos peixes!\n\n",
             "MSG_UHULL":"MODAFOCA",
             "MSG_DEU_RUIM":"Put a Keep are You... Full Del!",
             "MSG_":"Option only available in paid version.",
             "MSG_OPTIONS":"""#=======================================================#
#                      OPCOES                           #
# B - Baixar facilidade                                 #
# C - Contar e gerar arquivo de facilidades             #
# G - Gerar grafo de facilidade                         #
# P - Calcular facilidades que ainda nao foram faceis   #
# S - Sair da facilidade                                #
#=======================================================#""",
             "MSG_WELCOME":"""#=======================================================#
#                     GAMBIFACIL                        #
# Solucao em facilidades facilitadoras de coisas faceis #""",
             "MSG_ERRO":"ERROR: Error Message failed to pri"}
             



def get_options_interface():                                                    #Sim, soh para pegar o q o infeliz digita
    return raw_input().lower()

def msgs(msg):                                                                  #Deixar todas as msgs do programa aqui, mas facil de rastrear e alterar, acho...
    texts = messeges()
    print texts.msgs[msg]
