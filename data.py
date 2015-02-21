#Autores: Andre Coradin Gulin e Fernando P. Domingues.
#Arquivo de pegar dados putoes da web, mascar e cuspir em um arquivo
#se meter algo alem disso, sera metido novamente em seu anel de carne

import urllib2
from cookielib import CookieJar
import view as v

def get_zipfile():                                                                  #Ao inves de baixar pelo shellscript
                                                                                    #optei por fazer o python baixar a parada
    url = 'http://www1.caixa.gov.br/loterias/_arquivos/loterias/D_lotfac.zip'       #mais a frente tera uma funcao q extrai as paradas
    cj = CookieJar()                                                                #aqui o esquema eh q ele da uma bolacha(cookie) para um macaquinho
                                                                                    #e consegue pegar o arquivo zip lah do site
    v.feedback_messages(1)                                                          #aviso q vou comecar a baixar o arquivo
    
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))                  #abro a url
    f = opener.open(url)
    data = f.read()                                                                 #pego o arquivo
    with open("D_lotfac.zip", "wb") as code:                                
        code.write(data)                                                            #escrevo no diretorio corrente

    v.feedback_messages(2)                                                          #e ainda aviso na tela, mtu bom :)
    
