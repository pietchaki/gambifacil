#Autores: Andre Coradin Gulin e Fernando P. Domingues.
#Arquivo de pegar dados putoes da web, mascar e cuspir em um arquivo
#se meter algo alem disso, sera metido novamente em seu anel de carne

import urllib2
from urllib import urlopen
import re
import zipfile,os.path
from cookielib import CookieJar
import view as v

def get_zipfile():
    v.msgs("MSG_DOWN_JOGOS")                                                        #Ao inves de baixar pelo shellscript
                                                                                    #optei por fazer o python baixar a parada
    url = 'http://www1.caixa.gov.br/loterias/_arquivos/loterias/D_lotfac.zip'       #mais a frente tera uma funcao q extrai as paradas
    cj = CookieJar()                                                                #aqui o esquema eh q ele da uma bolacha(cookie) para um macaquinho
                                                                                    #e consegue pegar o arquivo zip lah do site

    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))                  #abro a url
    f = opener.open(url)
    data = f.read()                                                                 #pego o arquivo
    with open("D_lotfac.zip", "wb") as code:
        code.write(data)                                                            #escrevo no diretorio corrente
    v.msgs("MSG_DOWN_JOGOS_END")


def unzip(source_filename, dest_dir):                                               #uso biblioteca para tirar as facilidades do zip
    v.msgs("MSG_EXTRACT")                                                           #e ainda aviso na tela, mtu bom :)
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
    v.msgs("MSG_EXTRACT_END")


def get_numbers():
    mat_jogos = []
    v.msgs("MSG_FIND_JOGOS")
#   busca = (<td rowspan".*?">[0-9]{2,2}<td>){15,15}                                #python nao sabe brincar de grupos entao tive que abrir a parada toda:
    busca = re.compile('<td[^>]*?>[0-9]{2,2}</td>\s*<td[^>]*?>[0-9]{2,2}</td>\s*<td[^>]*?>[0-9]{2,2}</td>\s*<td[^>]*?>[0-9]{2,2}</td>\s*<td[^>]*?>[0-9]{2,2}</td>\s*<td[^>]*?>[0-9]{2,2}</td>\s*<td[^>]*?>[0-9]{2,2}</td>\s*<td[^>]*?>[0-9]{2,2}</td>\s*<td[^>]*?>[0-9]{2,2}</td>\s*<td[^>]*?>[0-9]{2,2}</td>\s*<td[^>]*?>[0-9]{2,2}</td>\s*<td[^>]*?>[0-9]{2,2}</td>\s*<td[^>]*?>[0-9]{2,2}</td>\s*<td[^>]*?>[0-9]{2,2}</td>\s*<td[^>]*?>[0-9]{2,2}</td>',re.DOTALL)
                                                                                    #busca recebe conjunto de 15 "jogos". jogos= "<td rowspan="###">##</td>"
                                                                                    # <td[^>]*?> -> pega o <td rowspan="###">
    try:                                                                                # \b         -> pega qualquer caractere branco no fim de uma "palavra"
        text = urlopen('file:D_LOTFAC.HTM').read()
        for dado in busca.findall(text):                                                # pega dados validos
            line = []
            dado = re.sub(r"<td[^>]*?>", "",dado)                                       # remove tags. Numeros sorteados ficam em uma unica linha, separados por espaco.
            dado = re.sub(r"</td>\s*", " ",dado)
            line = [int(s) for s in dado.split() if s.isdigit()]                        # http://stackoverflow.com/questions/4289331/python-extract-numbers-from-a-string
            if len(line) != 15:                                                         # bom garantir que nao estou fazendo cagada... hehehe
                print "############################################################"
                print "Jogo com "+len(line)+" numeros sorteados...."
                print dado
            else:
                mat_jogos.append( sorted( line ) )                                      #ordena e coloca linha na matriz
        mat_str_for_file = str(mat_jogos)                                               #Gero arquivo de saida apenas para conferencia
        mat_str_for_file = mat_str_for_file.replace("[","")
        mat_str_for_file = mat_str_for_file.replace(",","")
        mat_str_for_file = mat_str_for_file.replace("]","\n")
        with open("Results.txt", "w") as saida:
            saida.write(mat_str_for_file)
        v.msgs("MSG_FIND_JOGOS_END")
        return mat_jogos
    except IOError, e:
        v.msgs('MSG_DEU_RUIM')

