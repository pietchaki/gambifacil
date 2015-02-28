#Autores: Andre Coradin Gulin e Fernando P. Domingues.
#Arquivo de probabilidade e eh aqui q a porra fica seria pq nem eu
#sei oq vai aqui, mas eh tudo q nao vai nos outros arquivos
#tipo a putaria de grafos, e medicao da distancia da lua para calculo da influencia da gravidade sobre o peso das bolas, pq vai ajudar nas magias de acertar a parada
#com as probabilidades

# calcula ocorrencias de quadras
# eg.: quantas vezes quatro numeros foram sorteados juntos
# egg.: os numeros 03, 09, 17 e 22 foram sorteados juntos em 90 jogos.
# /!\ Func em estado pre-alpha... nao serve pra quase nada
def calcQuads():
    quad_count = [[[[0 for x in xrange(22)]for x in xrange(22)]for x in xrange(22)]for x in xrange(22)]
    for jogo in mat_jogos:
        for i in range(0, 12):
            for j in range(i+1, 13):
                for k in range(j+1, 14):
                    for l in range(k+1, 15):
                        quad_count[jogo[i]-1][jogo[j]-2][jogo[k]-3][jogo[l]-4] += 1

    #ll = len(mat_jogos)
    #for i in range(0, 22):
        #for j in range(i+1, 23):
            #for k in range(j+1, 24):
                #for l in range(k+1, 25):
                    #quad_count[i][j-1][k-2][l-3] = float(quad_count[i][j-1][k-2][l-3]) / float(ll)

    return quad_count
# "calcula" "probabilidade" de uma aposta, baseado em quantas vezes
# cada subconjunto de tamanho 4 ja foi sorteado.
def statQuads():
    print "statQuads:"
    #stat = [0 for x in xrange(len(mat_apostas))]
    quad_count = calcQuads()
    with open('stat_quad.txt', 'w+') as saida:
        for aposta in mat_apostas:
            stat = 1.0
            for i in range(0, 12):
                for j in range(i+1, 13):
                    for k in range(j+1, 14):
                        for l in range(k+1, 15):
                            #stat[a] += quad_count[aposta[i]-1][aposta[j]-2][aposta[k]-3][aposta[l]-4]
                            stat += quad_count[aposta[i]-1][aposta[j]-2][aposta[k]-3][aposta[l]-4]
                            print "{0:.32f}".format(stat)
            sys.exit(0)
            for n in aposta:
                saida.write(str(n)+",")
            saida.write("> " + str(stat) + "\n")

# conta tamanhos da intersessao dos conjuntos
def howEqual(a, b):
    return len(set(a) & set(b))

# Verifica se aposta eh parecida com algum jogo que jah saiu
# minEq -> minimo de elementos de <jogo> que estao em <aposta>
def isEqual(aposta, jogo, minEq, tam_aposta):
#    old, lazy version:
#    if howEqual(aposta, jogo) < minEq:
#        return False
#    else:
#        return True
    a=j=errA=errJ=0
    maxerrJ = 15 - minEq
    maxerrA = tam_aposta - minEq
    while a<tam_aposta and j<15 :
        if aposta[a] < jogo[j]:
            a+=1
            errA+=1
            if errA > maxerrA:
                return False
        elif jogo[j] < aposta[a]:
            j+=1
            errJ+=1
            if errJ > maxerrJ:
                return False
        else:
            a+=1
            j+=1
    return True

# remove apostas muito parecidos com jogos jah sorteados
def remove_invalidos(inicio, tam_aposta):
    global mat_apostas
    i=0
    x=len(mat_apostas)-1
    y=len(mat_jogos)-1
#    for jogo in mat_jogos:
#    for j in range(inicio,len(mat_jogos)):
    j=inicio
    while j<y:
        i=0
#        for aposta in mat_apostas:
        while i<x:
            if isEqual(mat_apostas[i], mat_jogos[j], 14, tam_aposta):
                del mat_apostas[i]
                x-=1
                break
            else:
                i+=1
        j+=1

# parte recorrente da funcao que gera todas as apostas possiveis...
def gera_n(seq, i, n):
    global mat_apostas # lista das apostas
    if i > 9:
        if (seq[i-1] - seq[i-10] == 9):                                             #evita gerar apostas com mais de 9 numeros em sequencia
            return
    for x in range(seq[i-1]+1,27-n+i):
        seq[i] = x;
        if(i>=n-1): # BASE
            mat_apostas.append(list(seq))
        else:
            so = gera_n(seq,i+1,n)

# le apostas do arquivo ou gera tudo do zero.
# retorna numero do ultimo jogo verificado
def le_apostas(n):
    global mat_apostas
    mat_apostas = []
    if os.path.exists('apostas_'+str(n)):        # se arquivo existe, le do arquivo
        print "Lendo arquivo..."
        with open('apostas_'+str(n), 'r') as f:
            verificados = int(string.split(f.readline())[0])
            #print verificados
            for line in f:
                aposta = [int(s) for s in line.split() if s.isdigit()]
                #print aposta
                mat_apostas.append(aposta)
        return verificados
    else:                                        # se aqruivo de apostas ainda nao existe, criamos um novo
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
    remove_invalidos(verificados,n)
    #print "apostas salvas: "+str(len(mat_apostas))
    # Salva em  arquivo
    if ap_lidas == len(mat_apostas):
        #print "tudo igual..."
        return
    print "salvando arquivo apostas_"+str(n)
    with open('apostas_'+str(n), 'w+') as saida:
        saida.write(str(len(mat_jogos))+" "+str(len(mat_apostas))) #escreve numero de apostas jah excluidas
        saida.write("\n")
        for jogo in mat_apostas:
            for j in jogo:
                saida.write("{0:2d} ".format(j))
            saida.write("\n")
    print "done."
    # calcula probabilidades...
# / calcula_apostas