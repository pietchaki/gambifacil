#include <pthreads.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>



int main(int argc, char **argv){
	int i, tam_aposta, inicio, max_err;
	char arq_jogos*="Resultados", arq_apostas[12];
	if(argc < 2){
		exit(1);
	}
	strcpy(arq_apostas,"apostas_");
	strcat(arq_apostas,argv[1]);
	tam_aposta = atoi(argv[1]);
	max_err = atoi(argv[2]);
	
// 	leJogos(arq_jogos);
// 	leApostas(arq_apostas);
	
// 	removeInvalidos();
	
// 	imprimeApostas();
	
}

/*
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
*/