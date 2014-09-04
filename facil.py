#!/usr/bin/env python

from urllib import urlopen
import re
import sys
import subprocess
from Tkinter import *

global mat_jogos

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
	global mat_jogos
	vetOcorr = [0] * 25
	vetPar   = [0] * len(matJogos)
	vetImpar = [0] * len(matJogos)
	vetParid = [0] * 2
	print "-------------> len(mat_jogos) = "+str(len(mat_jogos))
	print "-------------> len(matJogos) = "+str(len(matJogos))
	
	
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

	print "===================> len(matJogos) = "+str(len(matJogos))
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
