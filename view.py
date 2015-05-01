#Autores: Andre Coradin Gulin e Fernando P. Domingues.
#Arquivo de apresentacao de conteudo
#Colocar neste arquivo apenas codigos de coisas
#que serao aprentadas na tela ou codigos de tratamento das mesmas

class messeges:
    msgs = { "MSG_>":"> ",
             "MSG_DOWN_JOGOS":"Baixando zip de facilidades...",
             "MSG_DOWN_JOGOS_END":"Terminei de baixar facilidades, olhe a pasta local.",
             "MSG_EXTRACT":"Extraindo facilidades...",
             "MSG_GET_LUCKY":"Escolhendo facilidades...Aguarde",
             "MSG_GET_LUCKY_END":"Escolhi facilidades.",
             "MSG_GRAFANDO":"Grafando...Aguarde",
             "MSG_GRAFANDO_END":"Grafei.",
             "MSG_CAMINHANDO":"Caminhando...Aguarde",
             "MSG_CAMINHANDO_END":"Caminhei.",
             "MSG_EXTRACT_END":"Terminei de extrair facilidades.",
             "MSG_FIND_JOGOS":"Encontrando sequencias de facilidades...",
             "MSG_FIND_JOGOS_END":"Terminei de encontrar sequencias faceis",                        # ta tudo muito bonito, bora zoar... heheheh
             "MSG_END":"\n\tAdeus,\n\t   E obrigado pelos peixes!\n\n",
             "MSG_UHULL":"MODAFOCA",
             "MSG_DEU_RUIM":"Put a Keep are You... Full Del!",
             "MSG_":"Option only available in paid version.",                                       # a opcao b a seguir eh executada por padrao no comeco, esta ali apenas para recovery se der merda
             "MSG_OPTIONS":"""#=======================================================#
#                      OPCOES                           #
# A - Atualizar facilidade                              #
# B - Ler facilidades                                   #
# C - Contar e gerar arquivo de facilidades             #
# G - Gerar grafo de facilidade                         #
# L - Gerar facilidade sortuda                          #
# K - Adiciona dados temporais ao grafo (exec. G antes) #
# F - Gerar facilidade grafada                          #
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
