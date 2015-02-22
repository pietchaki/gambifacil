#Autores: Andre Coradin Gulin e Fernando P. Domingues.
#Arquivo de pegar dados putoes da web, mascar e cuspir em um arquivo
#se meter algo alem disso, sera metido novamente em seu anel de carne

import urllib2
import zipfile,os.path
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
    

def unzip(source_filename, dest_dir):                                               #uso biblioteca para tirar as facilidades do zip
    v.feedback_messages(3)    
    with zipfile.ZipFile(source_filename) as zf:                                    #peguei essa parada das webs e acredito q funciona
        for member in zf.infolist():                                                #na vdd, testei e funciona mesmo, entao eh isso ai

            words = member.filename.split('/')
            path = dest_dir
            for word in words[:-1]:
                drive, word = os.path.splitdrive(word)
                head, word = os.path.split(word)
                if word in (os.curdir, os.pardir, ''):
                    continue
                path = os.path.join(path, word)
            zf.extract(member, path)
    v.feedback_messages(4)    
