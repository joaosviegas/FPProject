########## Projeto 1 -> Vales e Montanhas ##########

# ---------- Notas Iniciais ----------

'''
Com o propósito de obter um código mais eficiente e sucinto, 
criei duas listas que reutilizei ao longo do projeto.
Deste modo, sempre que estas listas aparecerem, saiba-se que remetem para: 
'''

VERTICAL = [chr(i) for i in range(65,91)]
'''
Utilizada para converter as entradas do território em caminhos 
verticais de 'A' a 'Z', como também verificar se as interseções são válidas.
'''

HORIZONTAL = [i for i in range(1,100)]
'''
Utilizada para os mesmos fins que o VERTICAL, mas referentemente 
aos caminhos horizontais, convertendo-os para números de 1 a 99.
'''

''' 
Também criei funções auxiliares, as quais estão devidamente
identificada pelo prefixo " auxiliar_ ". 
'''

# ---------- 2.1.1 ----------

def eh_territorio(t):
    '''
    Classifica o argumento introduzido como um
    território válido (True) ou inválido (False).

    eh territorio: universal → booleano
    '''
    if type(t) != tuple or len(t) < 1 or len(t) > 26 or type(t[0]) != tuple:
        return False
    
    tamanho = len(t[0])

    for i in t:
        if type(i) != tuple or len(i) != tamanho or len(i) < 1 or len(i) > 99: # Se tiver um caminho com mais ou menos interseções -> False
            return False
        
        for j in i:
            if type(j) != int or j  !=0 and j !=1: # Se os valores dentro dos tuplos do tuplo forem != (0 or 1) -> False
                return False
    return True

# ---------- 2.1.2 ----------

def obtem_ultima_intersecao(t):
    '''
    Devolve a interseção do canto superior
    direito de um território introduzido.

    obtem ultima intersecao: territorio → intersecao
    '''
    return (VERTICAL[len(t)-1],HORIZONTAL[len(t[0])-1])

# ---------- 2.1.3 ----------

def eh_intersecao(arg):
     '''
     Classifica o argumento introduzido como
     uma interseção válida (True) ou inválida (False).

     eh intersecao: universal → booleano
     '''
     return type(arg) == tuple and  not len(arg) != 2 \
          and arg[0] in VERTICAL and arg[1] in HORIZONTAL \
          and type(arg[0]) == str and type(arg[1]) == int # Verifica o tamanho e elementos do argumento

# ---------- 2.1.4 ----------

def eh_intersecao_valida(t,i):
     '''
     Classifica se uma interseção de um território
     introduzido é válida (True) ou inválida (False).

     eh intersecao valida: territorio × intersecao → booleano
     '''
     if eh_territorio(t) and eh_intersecao(i): # Se não for um território ou interseção válida -> False
          
          for k in range(len(t)): # Percorre todos os Caminhos verticais do território
               if VERTICAL[k] == i[0]: # Verifica se a Letra existe na lista

                    for j in range(len(t[k])): # Se sim, percorre todos os Caminhos horizontais desse tuplo
                         if HORIZONTAL[j] == i[1]: # Verifica se o número existe na lista
                              return True 
          return False
     else:
          return False

# ---------- 2.1.5 ----------

'''
Decidi definir uma função auxiliar para obter os índices de uma interseção 
pois percebi-me que iria utilizar a mesma peça de código várias vezes nas funções seguintes.
'''

def auxiliar_indices(t,i):
     '''
     Função Auxiliar, que retorna os índices
     de uma dada interseção de um dado território.
     '''
     nv = i[0] # Guarda cada um dos elementos da interseção
     nh = i[1]

     for k in range(len(t)): # Guarda os valores das entradas do tuplo i no Nvertical (nh) e Nhorizontal (nv)  
          if VERTICAL[k] == nv: # Percorre todo o território até encontrar o tuplo com o valor de nv 
               v = k

               for j in range(len(t[v])): # Percorre todo o tuplo de indice v até encontrar a entrada com o valor de nh
                     if HORIZONTAL[j] == nh:
                         h = j
     return(v,h)

def eh_intersecao_livre(t,i):
     '''
     Classifica uma interseção de um território
     introduzido como uma interseção livre (True)
     ou inválida (False).

     eh intersecao livre: territorio × intersecao → booleano
     '''
     if eh_territorio(t) and eh_intersecao(i) and eh_intersecao_valida(t,i): # Verifica se os valores de t e i são territórios e interceções válidas                    
          if t[auxiliar_indices(t,i)[0]][auxiliar_indices(t,i)[1]] == 0: # Verifica se a entrada do tuplo[v][h] esta livre (=0) ou não (!=0)
               return True
     return False

# ---------- 2.1.6 ----------

def obtem_intersecoes_adjacentes(t,i):
    '''
    Devolve as interseções adajcentes a uma
    certa interseção de um território introduzido.

    obtem intersecoes adjacentes: territorio × intersecao → tuplo
    '''
    adjacentes = []
    contador = 0 # Conta
    flag = True # Defini uma flag para fazer as interceções na ordem desejada

    while contador < 4:

        for adicionar_1 in range(-1,2,2): # Utilizo este range para adicionar -1 ou 1, para obter as interseções adjacentes

            adj = (chr(65 + auxiliar_indices(t,i)[0]),auxiliar_indices(t,i)[1] + 1 + adicionar_1) # Baixo / Cima

            if eh_intersecao_valida(t,adj): #Se as interseções criadas forem válidas, adiciono-as a uma lista
                adjacentes += [adj]
            contador += 1

            if flag == True:

                for adicionar_2 in range(-1,2,2):

                    adj = (chr(65 + auxiliar_indices(t,i)[0] + adicionar_2),auxiliar_indices(t,i)[1] + 1) # Esquerda / Direita

                    if eh_intersecao_valida(t,adj):
                        adjacentes += [adj]
                    contador += 1
                flag = False # Após fazer as interseções da esquerda / direita, não volta a este "for"
      
    return tuple(adjacentes)

# ---------- 2.1.7 ----------

def ordena_intersecoes(tup):
    '''
    Ordena um tuplo contendo várias interseções,
    de acordo com a ordem pela qual são lidos num território.
    '''
    tup = sorted(tup) # Utilizo a função sorted para organizar a lista de interseções pelas letras (caminhos verticais)
    ordena = sorted(tup, key = lambda x: x[1]) # Depois utilizo o lambda com uma key para ordenar pelos números (caminho verticais)
               
    return tuple(ordena)
    
# ---------- 2.1.8 ----------
'''
Defini uma função axiliar para evitar a 
repetição redundante de código dentro da seguinte função.
'''

def auxiliar_letras_str(t):
    '''
    Função auxiliar, que transforma os 
    caminhos verticais de um território em letras.
    '''
    letras = ''

    for i in range(len(t)): # Percorre todo o território
        letras += ' ' + VERTICAL[i] # Adiciona a letra de cada caminho horizontal

    return letras    

def territorio_para_str(t):
    '''
    Devolve a representação visual de um
    território introduzido.

    territorio para str: territorio → cad. carateres
    '''
    if not eh_territorio(t):
        raise ValueError('territorio_para_str: argumento invalido')

    mapa = '  '

    mapa += auxiliar_letras_str(t)

    mapa += '\n'

    for i in range(len(t[0])-1,-1,-1): # Contador para os caminhos horizontais (números)
        
        mapa += '{:>2}' .format(str(HORIZONTAL[i])) + ' '

        linha = ''

        for j in range(len(t)): # Contador para percorrer todas as entradas do tuplo
            if t[j][i] == 0:
                linha += '.'
            else:
                linha += 'X' # Guardo cada linha do território pretendido

            linha += ' '

        mapa += linha # Adiciono-a linha-a-linha

        mapa += '{:>2}' .format(str(HORIZONTAL[i])) # Números da direita

        mapa += '\n'
        
    mapa += '  '

    mapa += auxiliar_letras_str(t)
    
    return mapa

# ---------- 2.2.1 ----------       

def obtem_cadeia(t,i):
    '''
    Devolve todas as interseções conectadas
    a uma interseção introduzida, desde que
    tenham o mesmo estado de ocupação, num
    dado território.

    obtem cadeia: territorio × intersecao → tuplo
    '''
    if not eh_territorio(t) or not eh_intersecao(i) or not eh_intersecao_valida(t,i):
        raise ValueError('obtem_cadeia: argumentos invalidos')
    
    cadeia = [i,]
    flag = eh_intersecao_livre(t,i)
    contador = 0 

    while contador != len(cadeia): # Enquanto o contador for diferente do tamanho da cadeia, adiciona elementos
        iterar = obtem_intersecoes_adjacentes(t,cadeia[contador]) # Criei uma lista para os elementos que vou verificar as adjacentes

        for e  in iterar:
            if eh_intersecao_livre(t,e) == flag and e not in cadeia : # Se forem adjacentes e não forem repetidas, adiciona à lista da cadeia
                cadeia += [e]
        contador+=1 # Depois de ver todos os elementos no iterar, aumento o contador e repete

    cadeia = tuple(cadeia)

    return ordena_intersecoes(cadeia)

# ---------- 2.2.2 ----------       

def obtem_vale(t,i):
    '''
    Devolve os vales de uma montanha, ou
    cadeia de montanhas, desde que a
    interseção dada seja uma montanha,
    num dado território.

    obtem vale: territorio × intersecao → tuplo
    '''
    if not eh_territorio(t) or not eh_intersecao(i) or not eh_intersecao_valida(t,i) or eh_intersecao_livre(t,i):
        raise ValueError('obtem_vale: argumentos invalidos')
    
    vale = []
    iterar = []
    cadeia = obtem_cadeia(t,i)
    
    for e in cadeia:
        iterar += obtem_intersecoes_adjacentes(t,e)  # Crio uma lista com todas as adjacentes da cadeia
    
        for j in iterar:
            if j not in cadeia and j not in vale: # Verifico se cada elemento é repetido ou se não faz parte da cadeia em si
                vale += [j]
    
    return ordena_intersecoes(vale)

# ---------- 2.3.1 ----------       

def verifica_conexao(t,i1,i2):
    '''
    Verifica se duas interseções introduzidas
    estão conectadas, num dado território.

    verifica conexao: territorio × intersecao ×-intersecao→booleano
    '''
    if not eh_territorio(t) or not eh_intersecao(i1) or not eh_intersecao(i2) or not eh_intersecao_valida(t,i1) or not eh_intersecao_valida(t,i2):
        raise ValueError('verifica_conexao: argumentos invalidos')
    
    return i1 in obtem_cadeia(t,i2) # Se estiverem cada um na cadeia do outro, estão conectados

# ---------- 2.3.2 ----------

def calcula_numero_montanhas(t):
    '''
    Devolve o número de montanhas
    existentes num dado território.

    calcula numero montanhas: territorio → int
    '''
    if not eh_territorio(t):
        raise ValueError('calcula_numero_montanhas: argumento invalido')

    numero_montanhas = 0

    for v in t: # Pecorre todos os tuplos do território

        for h in v: # Percorre todas as entradas desse tuplo
            if h == 1: # Se o valor da entrada for 1, adiciona-se +1 ao numero_montanhas
                numero_montanhas += 1

    return numero_montanhas

# ---------- 2.3.3 ----------

'''
Decidi definir uma função auxiliar para obter uma lista de todas as 
interseções existentes num território, pois iria utilizar a mesma 
funcionalidade nas 2 funções seguintes.
'''

def auxiliar_intersecoes(t):
    '''
    Função Auxiliar, que retorna 
    um tuplo com todos as interseções 
    de um território.
    '''
    todos = []

    for v in range(len(t)): # Percorre todos os tuplos do território

        for h in range(len(t[0])): # Percorre todos os elementos de cada tuplo
            todos += [(VERTICAL[v],HORIZONTAL[h])] # Adiciona cada interseção a uma lista

    return tuple(todos)

def calcula_numero_cadeias_montanhas(t):
    '''
    Devolve o número de cadeias de
    montanhas existentes num dado
    território.

    calcula numero cadeias montanhas: territorio → int
    '''
    if not eh_territorio(t):
        raise ValueError('calcula_numero_cadeias_montanhas: argumento invalido')
    
    cadeias = []
    numero_cadeias = 0
    iterar = auxiliar_intersecoes(t) # Irei iterar sobre a lista de todas as interseções

    for e in iterar:

        if not eh_intersecao_livre(t,(e[0],e[1])): # Se a interseção for uma montanha
              
              if e not in cadeias: # Se essa cadeia ainda não estiver na cadeias
                cadeias += obtem_cadeia(t,e)
                numero_cadeias += 1

    return numero_cadeias 

# ---------- 2.3.4 ----------

def calcula_tamanho_vales(t):
    '''
    Devolve o número de vales
    existentes num dado território.

    calcula tamanho vales: territorio → int
    '''
    if not eh_territorio(t):
        raise ValueError('calcula_tamanho_vales: argumento invalido')
    
    iterar = auxiliar_intersecoes(t) # Utilizo a lista com todas as interseções
    final = []
    cadeias = []

    for e in iterar: # Utilizo o memso algoritmo que no 2.3.3 para obter todas as cadeias

        if not eh_intersecao_livre(t,(e[0],e[1])):
                
                if e not in cadeias:
                    cadeias += obtem_cadeia(t,e) # Não pude utilizar uma função auxiliar pois necessitava do "numero_montanhas" no 2.3.3

    for e in cadeias:
        vales = obtem_vale(t,e) # Guardo os vales do elemento que estou a verificar

        for j in vales:
            if j not in final:
                final +=[j] # Se os vales não forem reptidos adiciono-os a uma lista

    return len(final)