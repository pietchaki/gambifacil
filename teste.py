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
            if isEqual(mat_apostas[i], mat_jogos[j], maxerr, tam_aposta):
            #if(len(set(mat_apostas[i]) & set(mat_jogos[j])) >= min_matches):
            # isEqual eh melhorzinho de leves que o metodo por sets...
                del mat_apostas[i]
                x-=1
                break
            else:
                i+=1
        j+=1
#/remove_invalidos

def getValues():
    busca = re.compile('<td[^\n]*?>../../....</td>.*?<td.*?>.*?,..</td>',re.DOTALL) # (data_sorteio ... arrecadacao)
    busca2 = re.compile('[0-9]{2,2}',re.DOTALL) # numero da bola
    #busca2 = re.compile('>..</td>',re.DOTALL) # numero da bola
    text = urlopen('file:D_LOTFAC.HTM').read()
    global mat_jogos
    mat_jogos = []

    for dado in busca.findall(text):        # pega dados validos
        line = []
        for s in busca2.findall(dado):  # pega numeros sorteados
            try:
                line.append( int(s) )   #colocar numero na linha
            except:
                print sys.exc_info()
        
        mat_jogos.append( sorted( line ) ) #ordena e coloca linha na matriz
    
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
# n = quantidade de numeros na aposta (15 a 20). ???????? como fazer?
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
    getValues()
    print "-------------> len(mat_jogos) = "+str(len(mat_jogos))
    #calcula_apostas(16)
    #print le_apostas(16)
    #print str(len(mat_apostas))

if __name__ == "__main__":
    main()