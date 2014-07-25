#!/usr/bin/env python

from urllib import urlopen
import re
import sys
import subprocess
from Tkinter import *
import os.path

global mat_jogos # jogos que jah sairam # tamanho de um jogo eh sempre 15
global mat_apostas # possiveis apostas  # tamanho de uma aposta eh >= 15

def remove_invalidos(inicio, maxerr):
	global mat_apostas
	jogos_ord = sorted(mat_jogos)
	min_matches = 15-maxerr
	i=0
	x=len(mat_apostas)
	y=len(jogos_ord)
	#for aposta in mat_apostas:
	while i<x:
		#for jogo in jogos_ord:
		for j in range(inicio,len(jogos_ord)):
			if(len(set(jogos_ord[j]) & set(mat_apostas[i])) >= min_matches):
				#print jogo
				print mat_apostas[i]
				#print set(jogo) & set(mat_apostas[i])
				del mat_apostas[i]
				x-=1
				inicio = j+1 # melhoria...
				#print ".",
				break
			j+=1
		else:
			i+=1
			continue
		#print ".",
		#print "----------------------------------------------------"
		#if i>3:
			#sys.exit()
	print x
#/remove_invalidos

def getValues():
	busca = re.compile('<td>../../....</td>.*?<td>.*?,..</td>',re.DOTALL) # (data_sorteio ... arrecadacao)
	text = urlopen('file:D_LOTFAC.HTM').read()
	busca2 = re.compile('<td>..</td>',re.DOTALL) # numero da bola
	global mat_jogos
	mat_jogos = []
	
	for dado in busca.findall(text): 		# pega dados validos
		line = []
		for s in busca2.findall(dado): 	# pega numeros sorteados
			s = s.replace("<td>","")
			s = s.replace("</td>","")
			try:
				line.append( int(s) )	#colocar numero na linha
			except:
				print sys.exc_info()
		mat_jogos.append( sorted( line ) ) #ordena e coloca linha na matriz
#/getValues



def gera_n(seq, i, n):
	global mat_apostas # lista dos jogos
	global saida
	for x in range(seq[i-1]+1,27-n+i):
		seq[i] = x;
		if(i>=n-1): # BASE
			mat_apostas.append(list(seq)) # TODO: fazer isso funcionar
		else:
			gera_n(seq,i+1,n)
# / gera_n

def le_apostas(n):
	global mat_apostas
	mat_apostas = []
	verificados = 0
	if os.path.exists('apostas_'+str(n)):
		with open('apostas_'+str(n), 'r') as f:
			verificados = int(f.readline())
			print verificados
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
			gera_n(seq, 1, n)
			print ".",
		print ""
		return 0

# jogos invalidos = jogos em q pelo menos 14 dos numeros nunca sairam
# n = quantidade de numeros na aposta (15 a 20). ???????? como fazer?
def calcula_apostas(n):
	if(n < 15 or n > 20):
		return 0
	verificados = le_apostas(n)
	print "total d apostas: "+str(len(mat_apostas))
	print "jogos validos:   "+str(len(mat_apostas)-len(mat_jogos))
	remove_invalidos(verificados,0)
	print "jogos calculados: "+str(len(mat_apostas))
	# Salva em  arquivo
	with open('apostas_'+str(n), 'w+') as saida:
		saida.write(str(len(mat_jogos))) #escreve numero de apostas jah excluidas
		for jogo in mat_apostas:
			for j in jogo:
				saida.write("{0:2d} ".format(j))
			saida.write("\n")
	# calcula probabilidades...
# / calcula_apostas

def main():
	getValues()
	calcula_apostas(15)
	#print le_apostas(16)
	#print str(len(mat_apostas))

if __name__ == "__main__":
	main()