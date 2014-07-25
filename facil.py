#!/usr/bin/env python

from urllib import urlopen
import re
import sys
import subprocess
from Tkinter import *

global mat_jogos

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

def imprime_resultados():
	global mat_jogos
	fResul = open ('Resultados','w+')
	for index in range(0,len(mat_jogos)):
		fResul.write('{0:4d} | '.format(index+1))
		for index2 in range(0,15):
			fResul.write('{0:3d}'.format(mat_jogos[index][index2]))
		fResul.write('  | Soma: {0:4d}'.format( sum(x for x in mat_jogos[index]))+'\n')
	fResul.close()		
	print "done"
#/imprime_resultados

def estatis(matJogos):
	vetOcorr = [0] * 25
	vetPar   = [0] * len(matJogos)
	vetImpar = [0] * len(matJogos)
	vetParid = [0] * 2

	
	for count in range(0,len(matJogos)):
		for index in range(0,15):
			vetOcorr[(matJogos[count][index])-1] += 1 
			if (matJogos[count][index] % 2 == 0):
				vetParid[0] += 1
				vetPar[count] += 1 
			else:
				vetParid[1] += 1
				vetImpar[count] += 1

	vetOcorrPar   = list(set(vetPar))
	vetOcorrImpar = list(set(vetImpar))

	for count in range(0,len(vetOcorrPar)):					# TODO eh feito um calculo desnecessario aqui, um loop eh suficiente
		temp = vetOcorrPar[count]							#pois a qnt de par eh o complemente de impar
		vetOcorrPar[count]= [temp, vetPar.count(temp)]

	for count in range(0,len(vetOcorrImpar)):
		temp = vetOcorrImpar[count]
		vetOcorrImpar[count]= [temp, vetImpar.count(temp)]

	fResul = open ('Estatisticas','w+')
	for index in range (0,25):	
		fResul.write(str(index+1)+' '+"{0:.2f}".format( float(vetOcorr[index]*100)/float(len(matJogos)) )+'%\n')
#		fResul.write(str(index+1)+' '+str( vetOcorr[index])+'\n')
	fResul.write('============================================================\n')

	for index in range(0,len(vetOcorrPar)):
		fResul.write('Qnt Pares: '+ str(vetOcorrPar[index][0])+ ' Ocorrencia: '+"{0:.2f}".format( float(vetOcorrPar[index][1]*100)/float(len(matJogos)) )+'%\n')
	fResul.write('\n')
	for index in range(0,len(vetOcorrImpar)):
		fResul.write('Qnt Impares: '+ str(vetOcorrImpar[index][0])+ ' Ocorrencia: '+"{0:.2f}".format( float(vetOcorrImpar[index][1]*100)/float(len(matJogos)) )+'%\n')
#	fResul.write('Total Pares: '+str(vetParid[0])+' Total Impares:'+str(vetParid[1])+'\n')   desnecessario
	fResul.close()
#/estatis

def callscript_baixa_resultado():
	subprocess.call(['./baixa_extrai_resultados.sh'])
	getValues()
	print "done"

def make_statistics():
	estatis(mat_jogos)
	print("done")

# verifica se um jogo ja saiu antes
# seq : jogo a ser testado
# maxerr: max erros para considerar dois jogos "iguais"
def ja_saiu(seq, maxerr):
	n = len(seq)
	for i in range(0, len(mat_jogos)):
		s = j = 0
		segundo = false
		nerr = maxerr
		while(s<n and j<15 and nerr>=0):
			if(seq[s] == mat_jogos[i][j]):
				i +=1
				j +=1
			elif(seq[s] < mat_jogos[i][j]):
				s +=1
			else: #if(seq[s] > mat_jogos[i][j]):
				nerr -=1
				j +=1
		#while
		if(j>=15-maxerr and nerr>=0):
			return true
	#for
	return false
#/ja_saiu

# func recursiva!
def gera_n(seq, i, n):
	global jogos_validos # lista dos jogos
	for x in range(seq[i-1],9+i):
		seq[i] = x;
		if(i>=n): # BASE
			# salva nalgum canto...
			jogos_validos.add(seq) # TODO: fazer isso funcionar
		else:
			gera_n(seq,i+1,n)
# / gera_n

# jogos invalidos = jogos em q pelo menos 14 dos numeros nunca sairam
# n = quantidade de numeros na aposta (15 a 20). ???????? como fazer?
def calcula_jogos_validos(n):
	if(n < 15 or n > 20):
		return 0
	# gera todos jogos possiveis
	gera_n(seq[n], 1, n)

	# Salva em  arquivo ??
	# calcula probabilidades...
# / calcula_jofos_validos


def make_grafico_soma():
        global mat_jogos
        newwindow = Toplevel()
        newwindow.title("Grafico Soma")
        largura = len(mat_jogos)
        graf = Canvas(newwindow, width=largura+3, height=151)
        graf.pack()
        graf.create_line(3,0,3,150)
        graf.create_line(3,150,largura,150)
        for index in range(0,len(mat_jogos)):
                y = 150-(sum(x for x in mat_jogos[index])-150)
                print y
                graf.create_line(index+4,y,index+5,y+1)
def start_gui():
	root = Tk()
	root.wm_title("Gambifacil")

	#TODO elementos da tela
	
	frame1 = Frame(root, height=400, width=400)
	frame1.pack()

	main_menu = Menu(root)
	main_menu.add_command(label="Baixar Resultados", command=callscript_baixa_resultado)
	main_menu.add_command(label="Imprimir Resultados", command=imprime_resultados)
	main_menu.add_command(label="Gerar Estatisticas", command=make_statistics)
	main_menu.add_command(label="Gerar Grafico de Somas", command=make_grafico_soma)
	root.config(menu=main_menu)
	
	root.mainloop()


def main():
	start_gui()


if __name__ == "__main__":
    main()
