#!/usr/bin/env python

from urllib import urlopen
import re
import sys
import string
import subprocess
from Tkinter import *
import os.path

global mat_jogos # jogos que jah sairam # tamanho de um jogo eh sempre 15
global mat_apostas # possiveis apostas  # tamanho de uma aposta eh >= 15
global quad_count

def quad_init():
    global quad_count
    quad_count = [[[[0 for x in xrange(22)]for x in xrange(22)]for x in xrange(22)]for x in xrange(22)]


# calcula ocorrencias de quadras
def calc_quads():
    quad_init()
    for jogo in mat_jogos:
        #print jogo
        for i in range(0, 12):
            for j in range(i+1, 13):
                for k in range(j+1, 14):
                    for l in range(k+1, 15):
                        #print i,j,k,l
                        #print jogo[i]-1,jogo[j]-2,jogo[k]-3,jogo[l]-4
                        #x=quad_count[jogo[i]-1][jogo[j]-2][jogo[k]-3][jogo[l]-4]
                        quad_count[jogo[i]-1][jogo[j]-2][jogo[k]-3][jogo[l]-4] += 1
    for i in range(0, 12):
        for j in range(i+1, 13):
            for k in range(j+1, 14):
                for l in range(k+1, 15):
                    print str(i+1)+", "+str(j+1)+", "+str(k+1)+", "+str(l+1)+" => "+str(quad_count[jogo[i]-1][jogo[j]-2][jogo[k]-3][jogo[l]-4])

# verifica quantos jogos parecidos ja sairam
def calc_parecidos():
    c1=c2=n1=n2=0
    i=j=0

    for i in range(0,len(mat_jogos)-1):
        for j in range(i+1,len(mat_jogos)):
            n = howEqual(mat_jogos[i], mat_jogos[j])
            #if n == 14:
                #print i, mat_jogos[i]
                #print j, mat_jogos[j]
                #print "-----------------------------"
            if n == n1:
                c1 += 1
            elif n == n2:
                c2 += 1
            elif n > n1:
                n2 = n1; n1 = n
                c2 = c1; c1 = 1
            elif n > n2:
                n2 = n
                c2 = 1
    print "teve "+str(c2)+" jogos com "+str(n2)+" numeros iguais"
    print "teve "+str(c1)+" jogos com "+str(n1)+" numeros iguais"


## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ##
## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ##
## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ##

# Verifica se aposta eh parecida com algum jogo que jah saiu
#maxerr -> maximo de elementos de <jogo> que nao estao em <aposta>
def isEqual(aposta, jogo, maxerr, tam_aposta):
    a=j=errA=errJ=0
    maxerrA = tam_aposta-15+maxerr
    while a<tam_aposta and j<15 :
        if aposta[a] < jogo[j]:
            a+=1
            errA+=1
            if errA > maxerrA:
                return False
        elif jogo[j] < aposta[a]:
            j+=1
            errJ+=1
            if errJ > maxerr:
                return False
        else:
            a+=1
            j+=1
    return True

# conta numeros na intersessao
def howEqual(a, b):
    return len(set(a) & set(b))




def remove_invalidos(inicio, maxerr, tam_aposta):
    global mat_apostas
    #min_matches = 15-maxerr
    i=0
    x=len(mat_apostas)-1
    y=len(mat_jogos)-1
    #for jogo in mat_jogos:
    #for j in range(inicio,len(mat_jogos)):
    j=inicio
    while j<y:
        i=0
        #for aposta in mat_apostas:
        while i<x:
            # isEqual eh melhorzinho de leves que o metodo por intersecao...
            if isEqual(mat_apostas[i], mat_jogos[j], maxerr, tam_aposta):
            #if(len(set(mat_apostas[i]) & set(mat_jogos[j])) >= min_matches):
                del mat_apostas[i]
                x-=1
                break
            else:
                i+=1
        j+=1
#/remove_invalidos


def getValues():
    global mat_jogos
    mat_jogos = []
    #busca recebe conjunto de 15 "jogos". jogos= "<td rowspan="###">##</td>"
    #busca = (<td rowspan".*?">[0-9]{2,2}<td>){15,15} #python nao sabe brincar de grupos entao tive que abrir a parada toda...
    # <td[^>]*?> -> pega o <td rowspan="###">
    # \b         -> pega qualquer caractere branco no fim de uma "palavra"
    busca = re.compile('<td[^>]*?>[0-9]{2,2}</td>\s*<td[^>]*?>[0-9]{2,2}</td>\s*<td[^>]*?>[0-9]{2,2}</td>\s*<td[^>]*?>[0-9]{2,2}</td>\s*<td[^>]*?>[0-9]{2,2}</td>\s*<td[^>]*?>[0-9]{2,2}</td>\s*<td[^>]*?>[0-9]{2,2}</td>\s*<td[^>]*?>[0-9]{2,2}</td>\s*<td[^>]*?>[0-9]{2,2}</td>\s*<td[^>]*?>[0-9]{2,2}</td>\s*<td[^>]*?>[0-9]{2,2}</td>\s*<td[^>]*?>[0-9]{2,2}</td>\s*<td[^>]*?>[0-9]{2,2}</td>\s*<td[^>]*?>[0-9]{2,2}</td>\s*<td[^>]*?>[0-9]{2,2}</td>',re.DOTALL)
    text = urlopen('file:D_LOTFAC.HTM').read()

    i = 0
    for dado in busca.findall(text):        # pega dados validos
        line = []

        # remove tags. Numeros sorteados ficam em uma unica linha, separados por espaco.
        dado = re.sub(r"<td[^>]*?>", "",dado)
        dado = re.sub(r"</td>\s*", " ",dado)
        #print dado

        line = [int(s) for s in dado.split() if s.isdigit()] # http://stackoverflow.com/questions/4289331/python-extract-numbers-from-a-string

        # DEBUG
        if len(line) != 15: # bom garantir que nao estou fazendo cagada... hehehe
            print "############################################################"
            print "Jogo com "+len(line)+" numeros sorteados...."
            print dado
        else:
        # /DEBUG
            mat_jogos.append( sorted( line ) ) #ordena e coloca linha na matriz
        i+=1
    #print i DEBUG
#/getValues



def gera_n(seq, i, n):
    global mat_apostas # lista dos jogos
    global saida
    if i > 9:
        if (seq[i-1] - seq[i-10] == 9):
            return
    for x in range(seq[i-1]+1,27-n+i):
        seq[i] = x;
        if(i>=n-1): # BASE
            mat_apostas.append(list(seq)) # TODO: fazer isso funcionar
        else:
            so = gera_n(seq,i+1,n)
# / gera_n

def le_apostas(n):
    global mat_apostas
    mat_apostas = []
    verificados = 0
    if os.path.exists('apostas_'+str(n)):
        print "Lendo arquivo..."
        with open('apostas_'+str(n), 'r') as f:
            verificados = int(string.split(f.readline())[0])
            #print verificados
            for line in f:
                aposta = [int(s) for s in line.split() if s.isdigit()]
                #print aposta
                mat_apostas.append(aposta)
        return verificados
    else:
        print "arquivo \'apostas_"+str(n)+"\' nao foi encontrado.\n criando arquivo novamente.\n /!\\ pode demorar varios minutos... /!\\"
        seq = [0]*n
        for i in range(1, 27-n):
            seq[0] = i
            so = gera_n(seq, 1, n)
            print ".",
        print ""
        return 0

# jogos invalidos = jogos em q pelo menos 14 dos numeros nunca sairam
# n = quantidade de numeros na aposta (15 a 20). 
def calcula_apostas(n):
    if(n < 15 or n > 20):
        return 0
    verificados = le_apostas(n)
    ap_lidas = len(mat_apostas)
    print "apostas lidas: "+str(ap_lidas)
    remove_invalidos(verificados,1,n)
    print "apostas salvas: "+str(len(mat_apostas))
    # Salva em  arquivo
    if ap_lidas == len(mat_apostas):
        print "tudo igual..."
        return
    with open('apostas_'+str(n), 'w+') as saida:
        saida.write(str(len(mat_jogos))+" "+str(len(mat_apostas))) #escreve numero de apostas jah excluidas
        saida.write("\n")
        for jogo in mat_apostas:
            for j in jogo:
                saida.write("{0:2d} ".format(j))
            saida.write("\n")
    # calcula probabilidades...
# / calcula_apostas

def main():
    if len(sys.argv) >1:
        if sys.argv[1] == "-d":
            subprocess.call(['./baixa_extrai_resultados.sh'])
    getValues()
    #calc_quads()
    #calc_parecidos()
    print "-------------> len(mat_jogos) = "+str(len(mat_jogos))
    calcula_apostas(16)
    #print str(len(mat_apostas))

if __name__ == "__main__":
    main()