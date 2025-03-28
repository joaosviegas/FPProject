########## Projeto 2 -> Go ##########

# ---------- Notas Iniciais ----------
'''
Neste projeto, à semelhança do primeiro, defini duas listas como variáveis 
globais com o propósito de obter um código mais limpo e sucinto;
Deste modo, sempre que estas listas aparecerem, saiba-se que remetem para: 
'''

LINHAS = [i for i in range(1,20)]
'''
Utilizada para converter as entradas do Goban em linhas 
numeradas de 1 a 19, (de acordo com o tamanho do Goban), 
como também verificar se as interseções são válidas.
'''

COLUNAS = [chr(i) for i in range(65,84)]
'''
Utilizada para converter as entradas do Goban em colunas 
de 'A' a 'S', (de acordo com o tamanho do Goban), 
como também verificar se as interseções são válidas.
'''

# ---------- 2.1.1 ----------

# ---------- Construtores ----------

def cria_intersecao(col,lin):
    '''
    Devolve a interseção no tabuleiro 
    correspondente a um caracter e um 
    número introduzidos.

    cria_intersecao: str × int → intersecao
    '''
    if type(col) != str or len(col) != 1 or \
        col not in COLUNAS or type(lin) != int or lin not in LINHAS:
            raise ValueError('cria_intersecao: argumentos invalidos')
        # Verifica a validade dos argumentos

    return (col,lin) # Devolve como um tuplo

# ---------- SELETORES ----------

def obtem_col(i):
    '''
    Devolve a letra da coluna de uma 
    dada interseção introduzida.

    obtem_col: intersecao → str
    '''
    return i[0]

def obtem_lin(i):
    '''
    Devolve o número da linha de uma 
    dada interseção introduzida.

    obtem_lin: intersecao → int
    '''
    return i[1]

# ---------- Reconhecedores ----------

def eh_intersecao(arg):
    '''
    Verifica se um dado argumento é 
    uma interseção válida (True) ou inválida (False).

    eh_intersecao: universal → booleano
    '''
    return isinstance(arg,tuple) and len(arg) == 2 and \
        isinstance(obtem_col(arg),str) and \
            len(arg) == 2 and isinstance(obtem_lin(arg),int) and \
                obtem_col(arg) in COLUNAS and obtem_lin(arg) in LINHAS

    # Verifica o tamanho, tipo e validade dos argumentos introduzidos

# ---------- Testes ----------

def intersecoes_iguais(i1,i2):
    '''
    Verifica se duas interseções introduzidas 
    são iguais (True) ou não (False).

    intersecoes_iguais: universal × universal → booleano
    '''
    return obtem_col(i1) == obtem_col(i2) and \
        obtem_lin(i1) == obtem_lin(i2)

# ---------- Transformadores ----------

def intersecao_para_str(i):
    '''
    Devolve a cadeia de caracteres que 
    representa a interseção introduzida.

    intersecao_para_str: intersecao → str
    '''
    return obtem_col(i) + str(obtem_lin(i)) # Converte para string e concatena

def str_para_intersecao(s):
    '''
    Devolve a interseção representada 
    pela string introduzida.

    str_para_intersecao: str → intersecao
    '''
    return cria_intersecao(s[0],int(s[1:])) # Converte os números para integer

# ---------- Funções Alto Nível ----------

def obtem_intersecoes_adjacentes(i,l):
    '''
    Obtem as interseções adjacentes a uma 
    dada interseção introduzida, pela ordem de 
    leitura em que a segunda interseção é a interseção 
    superior direita do tabuleiro de Go.

    obtem_intersecoes_adjacentes: intersecao × intersecao → tuplo
    '''
    adjacentes = []
    contador = 0
    flag = True # Defini uma flag para fazer as interceções pela ordem desejada

    if eh_intersecao(i) and obtem_col(i) <= obtem_col(l) and \
        obtem_lin(i) <= obtem_lin(l):

        while contador < 4: # Enquanto não verificar as 4 adjacentes possíveis

            # Utilizo este range para adicionar -1 ou 1, obtendo as interseções adjacentes
            for adicionar_1 in range(-1,2,2):

                adj = (chr(65 + (COLUNAS.index(obtem_col(i)))), \
                       (LINHAS.index(obtem_lin(i))) + 1 + adicionar_1) # Baixo / Cima

                if eh_intersecao(adj) and \
                    obtem_col(adj) <= obtem_col(l) and \
                        obtem_lin(adj) <= obtem_lin(l): #Verifico se são válidas
                    
                    adjacentes += [adj]

                contador += 1

                if flag == True:

                    for adicionar_2 in range(-1,2,2):

                        adj = (chr(65 + (COLUNAS.index(obtem_col(i))) + adicionar_2), \
                               (LINHAS.index(obtem_lin(i))) + 1) # Esquerda / Direita

                        if eh_intersecao(adj) and \
                            obtem_col(adj) <= obtem_col(l) and \
                                obtem_lin(adj) <= obtem_lin(l):
                            
                            adjacentes += [adj]

                        contador += 1

                    flag = False # Após fazer as da esquerda / direita, não volta ao 2º for
      
    return tuple(adjacentes)

def ordena_intersecoes(t):
    '''
    Ordena as interseções do tuplo introduzido 
    de acordo com a ordem de leitura no tabuleiro de Go.

    ordena_intersecoes: tuplo → tuplo
    '''
    return tuple(sorted(t, key = lambda x: (x[1], x[0])))
    # Ordena por números x[1] e depois por letras x[0]

# ---------- 2.1.2 ----------

# ---------- Construtores ----------

def cria_pedra_branca():
    '''
    Devolve uma pedra pertencente 
    ao jogador branco.

    cria_pedra_branca: {} → pedra
    '''
    return 0

def cria_pedra_preta():
    '''
    Devolve uma pedra pertencente 
    ao jogador preto.

    cria_pedra_preta: {} → pedra
    '''
    return 1

def cria_pedra_neutra():
    '''
    Devolve uma pedra que não 
    pertence a nenhum dos jogadores.

    cria_pedra_neutra: {} → pedra
    '''
    return 2

# ---------- Reconhecedores ----------

def eh_pedra(arg):
    '''
    Verfica se um argumento introduzido é 
    uma pedra (True) ou não (False).

    eh_pedra: universal → booleano
    '''
    return arg in (cria_pedra_branca(), cria_pedra_preta(), cria_pedra_neutra())

def eh_pedra_branca(p):
    '''
    Verifica se uma pedra é do jogador 
    branco (True) ou não (False).

    eh_pedra_branca: pedra → booleano
    '''
    return p == cria_pedra_branca()

def eh_pedra_preta(p):
    '''
    Verifica se uma pedra é do jogador 
    preto (True) ou não (False).

    eh_pedra_preta: pedra → booleano
    '''
    return p == cria_pedra_preta()

# ---------- Testes ----------

def pedras_iguais(p1,p2):
    '''
    Verifica se duas pedras são do mesmo tipo.

    pedras_iguais: universal × universal → booleano
    '''
    return (p1 == cria_pedra_preta() and p2 == cria_pedra_preta()) or \
        (p1 == cria_pedra_branca() and p2 == cria_pedra_branca()) or \
            (p1 == cria_pedra_neutra() and p2 == cria_pedra_neutra())

# ---------- Transformadores ----------

def pedra_para_str(p):
    '''
    Devolve a cadeia de caracteres que 
    representa o jogador dono da pedra.

    pedra_para_str: pedra → str
    '''
    if eh_pedra_preta(p):
        return 'X'
    
    if eh_pedra_branca(p):
        return 'O'
    
    return '.' # Se não for nem preta nem branca, é neutra

# ---------- Funções Alto Nível ----------

def eh_pedra_jogador(p):
    '''
    Verifica se uma pedra é de um dos 
    jogadores (True) ou não (False).

    eh_pedra_jogador: pedra → booleano
    '''
    return eh_pedra_preta(p) or eh_pedra_branca(p)

# ---------- 2.1.3 ----------

# ---------- Construtores ----------

def cria_goban_vazio(n):
    '''
    Devolve um tabuleiro de Goban vazio de tamanho n x n, 
    desde que n seja um dos tamanhos válidos.

    cria_goban_vazio: int → goban
    '''
    if n not in (9, 13, 19) or type(n) != int:
        raise ValueError('cria_goban_vazio: argumento invalido')
    
    contador_lin = 0
    goban = {} # Representei o Goban como um dicionário

    while contador_lin < n: # Enquanto não se atinjir o nº de linhas do tabuleiro

        contador_col = 0 # Inicia-se o contador das colunas

        goban[COLUNAS[contador_lin]] = {} # Adiciona-se uma entrada com a letra da coluna

        while contador_col < n: # Enquanto não se atinjir o nº de colunas do tabuleiro

            goban[COLUNAS[contador_lin]][LINHAS[contador_col]] = cria_pedra_neutra()
            # Adiciona-se uma entrada com o nº da linha

            contador_col += 1

        contador_lin += 1

    return goban

def cria_goban(n, ib, ip):
    '''
    Devolve um tabuleiro de Goban de tamanho n x n, 
    com as interceções ib preenchidas com pedras brancas 
    e as interseções ip preenchidas com pedras pretas.

    cria_goban: int × tuplo × tuplo → goban
    '''
    intersecoes = []
    if n not in (9, 13, 19) or type(n) != int or \
        not isinstance(ib,tuple) or not isinstance(ip, tuple):
        raise ValueError('cria_goban: argumentos invalidos')
    
    goban = cria_goban_vazio(n) # Cria-se um Goban vazio para preencher

    for e in ib + ip: # Verfica-se se todos os elementos das listas são tuples e interseções válidas

        if eh_intersecao(e) and \
            eh_intersecao_valida(goban, e) and \
                e not in intersecoes:
            intersecoes += [e]
        else:
            raise ValueError('cria_goban: argumentos invalidos')

    for branca in ib: # Percorre-se toda a lista de interseções com pedras brancas

        contador_lin = 0

        while contador_lin < n: # Percorre-se todas as linhas do goban

            contador_col = 0

            if COLUNAS[contador_lin] == obtem_col(branca): # Se a coluna for igual à coluna da interseção

                while contador_col < n: # Percorre-se essa coluna
                    
                    if LINHAS[contador_col] == obtem_lin(branca): # Se a linha for igual à linha da interseção
                        
                        goban[COLUNAS[contador_lin]][LINHAS[contador_col]] = cria_pedra_branca()
                        # Essa interseção passa a ter uma pedra branca

                    contador_col += 1

            contador_lin += 1

    for preta in ip: # Faz-se a mesma coisa para as pedras pretas
        
        contador_lin = 0

        while contador_lin < n:

            contador_col = 0

            if COLUNAS[contador_lin] == obtem_col(preta):

                while contador_col < n:
                    
                    if LINHAS[contador_col] == obtem_lin(preta):
                        
                        goban[COLUNAS[contador_lin]][LINHAS[contador_col]] = cria_pedra_preta()

                    contador_col += 1

            contador_lin += 1            

    return goban

def cria_copia_goban(t):
    '''
    Devolve uma cópia de um Goban introduzido.

    cria_copia_goban: goban → goban
    '''
    goban = cria_goban_vazio(obtem_lin(obtem_ultima_intersecao(t)))
    contador_lin = 0

    while contador_lin < obtem_lin(obtem_ultima_intersecao(goban)): 

        while contador_lin < obtem_lin(obtem_ultima_intersecao(goban)): # Percorre-se todas as linhas do Goban

            contador_col = 0

            while contador_col < obtem_lin(obtem_ultima_intersecao(goban)): # Percorre-se todas as colunas do Goban
                    
                    goban[COLUNAS[contador_lin]][LINHAS[contador_col]] = t[COLUNAS[contador_lin]][LINHAS[contador_col]]
                    # Iguala-se a interseção da cópia à do original

                    contador_col += 1

            contador_lin += 1

    return goban

# ---------- Seletores ----------

def obtem_ultima_intersecao(g):
    '''
    Devolve a interseção do canto superior 
    direito do Goban introduzido.

    obtem_ultima_intersecao: goban → intersecao
    '''
    return cria_intersecao(COLUNAS[len(g)-1],LINHAS[len(g)-1])

def obtem_pedra(g,i):
    '''
    Devolve a pedra que ocupa a interseção 
    introduzida no Goban introduzido.

    obtem_pedra: goban × intersecao → pedra
    '''
    return g[obtem_col(i)][obtem_lin(i)]

def obtem_cadeia(g,i):
    '''
    Devolve a cadeia de interseções ocupadas 
    por pedras do mesmo tipo que a interseção 
    introduzida, num dado Goban.

    obtem_cadeia: goban × intersecao → tuplo
    '''
    cadeia = [i,] # Começa-se a cadeia com a interseção introduzida
    contador = 0

    while contador < len(cadeia):

        iterar = obtem_intersecoes_adjacentes(cadeia[contador], obtem_ultima_intersecao(g))
        # Itera-se sobre as adjacentes das interseções já na cadeia

        for adjacente in iterar:

            if pedras_iguais(obtem_pedra(g, adjacente),obtem_pedra(g,i)) and \
                  adjacente not in cadeia:
                  # Se a interseção tiver o mesmo tipo de pedra e não for repetida
                cadeia += [adjacente]

        contador += 1
    
    return ordena_intersecoes(tuple(cadeia))

# ---------- Modificadores ----------

def coloca_pedra(g,i,p):
    '''
    Devolve o Goban depois de ser colocada 
    uma pedra numa dada interseção.

    coloca_pedra: goban × intersecao × pedra → goban
    '''
    # Utiliza-se o mesmo algoritmo de procura do cria_goban
    contador_lin = 0

    while contador_lin < len(g):

        contador_col = 0

        if (COLUNAS[contador_lin]) == obtem_col(i):

            while contador_col < len(g):
   
                if LINHAS[contador_col] == obtem_lin(i):
                    
                    g[COLUNAS[contador_lin]][LINHAS[contador_col]] = p
                    # A interseção passa a ser a pedra introduzida

                contador_col += 1

        contador_lin += 1            

    return g

def remove_pedra(g,i):
    '''
    Devolve o Goban depois de ser retirada 
    uma pedra de uma dada interseção.

    remove_pedra: goban × intersecao → goban
    '''
    # Utiliza-se o mesmo algoritmo do coloca_pedra

    contador_lin = 0

    while contador_lin < obtem_lin(obtem_ultima_intersecao(g)):

        contador_col = 0

        if (COLUNAS[contador_lin]) == obtem_col(i):

            while contador_col < obtem_lin(obtem_ultima_intersecao(g)):
   
                if LINHAS[contador_col] == obtem_lin(i):
                    
                    g[COLUNAS[contador_lin]][LINHAS[contador_col]] = cria_pedra_neutra()
                    # A interseção passa a ser uma pedra neutra

                contador_col += 1

        contador_lin += 1            

    return g

def remove_cadeia(g,t):
    '''
    Devolve o Goban depois de serem retiradas
    as pedras de uma dado conjunto de interseções.

    remove_cadeia: goban × tuplo → goban
    '''
    for inter in t: # Remove cada pedra das interseções dadas 
        remove_pedra(g, inter) 

    return g
    
def eh_goban(g):
    '''
    Verifica se um Goban introduzido 
    é válido (True) ou inválido (False).

    eh_goban: universal → booleano
    '''
    if type(g) != dict or \
        obtem_lin(obtem_ultima_intersecao(g)) not in (9,13,19): # Verifica-se o tipo e o número de linhas
            return False

    for coluna in g: # Verifica-se cada coluna do Goban

        if type (g[coluna]) != dict or len(g[coluna]) != \
            obtem_lin(obtem_ultima_intersecao(g)) or \
            coluna not in [chr(i) for i in range(65,65 + obtem_lin(obtem_ultima_intersecao(g)) )]:
                return False
         
        for linha in g[coluna]: # Verifica-se cada linha do Goban

            if not eh_pedra(g[coluna][linha]) or \
                type(linha) != int or linha not in LINHAS:
                return False
    return True        

def eh_intersecao_valida(g,i):
    '''
    Verifica se uma interseção é 
    válida para um dado Goban (True) 
    ou não (False).

    eh_intersecao_valida: goban × intersecao → booleano
    '''
    return eh_goban(g) and eh_intersecao(i) and \
        obtem_col(i) <= obtem_col(obtem_ultima_intersecao(g)) and \
            obtem_lin(i) <= obtem_lin(obtem_ultima_intersecao(g))

# ---------- Testes ----------

def gobans_iguais(g1,g2):
    '''
    Verifica se dois Gobans são 
    idênticos (True) ou não (Falso).

    gobans_iguais: universal × universal → booleano
    '''
    if eh_goban(g1) and eh_goban(g2) and \
        obtem_lin(obtem_ultima_intersecao(g1)) == \
            obtem_lin(obtem_ultima_intersecao(g2)): # Verifica-se a validade e os tamanhos 

        for contador in range(obtem_lin(obtem_ultima_intersecao(g1))): # Percorre-se todas as entradas dos Gobans

            if g1[COLUNAS[contador]] != g2[COLUNAS[contador]]: # Se forem diferentes -> False 
                return False
            
        return True
        
    return False

# ---------- Transformadores ----------
'''
Defini uma função auxiliar para evitar a repetição 
redundante de código dentro da seguinte função.
'''
def auxiliar_letras_para_str(g):
    '''
    Função auxiliar que devolve as 
    letras que representam as colunas 
    de um Goban introduzido.

    auxiliar_letras_para_str: goban → str
    '''
    letras = '  '

    for contador in range(obtem_lin(obtem_ultima_intersecao(g))):

        letras += ' ' + COLUNAS[contador]

    return letras

def goban_para_str(g):
    '''
    Devolve a representação gráfica 
    de um Goban introduzido.

    goban_para_str: goban → str
    '''
    goban = ''

    goban += auxiliar_letras_para_str(g)
    # Adiciona-se as letras de cima
    goban += '\n'

    for c_linha in range(obtem_lin(obtem_ultima_intersecao(g)),0,-1):

        goban += '{:>2}'.format(c_linha) + ' '

        linha = ''

        for c_coluna in range(obtem_lin(obtem_ultima_intersecao(g))):
        
            linha += pedra_para_str(g[COLUNAS[c_coluna]][c_linha]) + ' '
            # Percorre-se cada linha do Goban e adiciona-se uma a uma
        goban += linha

        goban += '{:>2}'.format(c_linha)

        goban += '\n'

    goban += auxiliar_letras_para_str(g)
    # Adiciona-se as letras de cima

    return goban    

# ---------- Funções Alto Nível ----------
'''
Defini uma função auxiliar pois iria utilizar 
esta funcionalidade em várias funçóes.
'''
def auxiliar_intersecoes(g):
    '''
    Função Auxiliar, que retorna 
    o conjunto de todas as interseções 
    de um Goban.

    auxiliar_intersecoes: goban → tup
    '''
    todos = []

    for col in range(obtem_lin(obtem_ultima_intersecao(g))): # Percorre todos as colunas

        for lin in range(obtem_lin(obtem_ultima_intersecao(g))): # Percorre todos as linhas

            todos += [cria_intersecao(COLUNAS[col],LINHAS[lin])] # Adiciona cada interseção a uma lista

    return tuple(todos)

def obtem_territorios(g):
    '''
    Devolve um tuplo com as interseções 
    do Goban pertencentes a cada território, 
    ordenadas pela ordem de leitura do tabuleiro.

    obtem_territorios: goban → tuplo
    '''
    territorios = []
    
    for inter in auxiliar_intersecoes(g):

        if not eh_pedra_jogador(g[obtem_col(inter)][obtem_lin(inter)]): # Se a interseção for neutra

            iterar = obtem_cadeia(g, inter)

            if iterar not in territorios: #Se essa cadeia não for repetida, adiciona-se
                territorios += [iterar]

    return tuple(sorted(territorios, key = lambda x: x[0][1]))
          

def obtem_adjacentes_diferentes(g,t):
    '''
    Devolve um tuplo ordenado com as interceções 
    adjacentes as interseções de um dado tuplo 
    introduzido, num dado goban;

    Se as interseções forem livres, devolve as 
    interseções com pedras (Fronteira do Território), 
    senão, devolve as interseções livres adjacentes 
    (Liberdades de uma Cadeia de Pedras).

    obtem_adjacentes_diferentes: goban × tuplo → tuplo
    '''
    diferentes = []
    
    for inter in t:

        flag = eh_pedra_jogador(g[obtem_col(inter)][obtem_lin(inter)]) # Flag para identificar se a interseção está livre ou não

        iterar = obtem_intersecoes_adjacentes(inter,obtem_ultima_intersecao(g)) # Obtem-se as adjacentes de cada elemento

        for j in iterar:

            if eh_pedra_jogador(g[obtem_col(j)][obtem_lin(j)]) != flag and j not in diferentes: # Adidiona-se se forem diferenets da flag e não repetidas
                diferentes += [j]
                    
    return ordena_intersecoes(tuple(diferentes))

def jogada(g,i,p):
    '''
    Devolve o próprio Goban, após ser colocada 
    uma pedra numa interseção, por um dos jogadores.
    
    jogada: goban × intersecao × pedra → goban
    '''
    goban = coloca_pedra(g,i,p)
    adjacentes = obtem_intersecoes_adjacentes(i, obtem_ultima_intersecao(goban))
    
    # Primeiro, verifica-se as adjacentes
    for e in adjacentes:

        if not pedras_iguais(obtem_pedra(goban, e), obtem_pedra(g,i)):
            cadeia = obtem_cadeia(goban, e)

            # Se não tiver liberdades, remove-se a cadeia
            if obtem_adjacentes_diferentes(goban, cadeia) == ():
                remove_cadeia(goban,cadeia)

    # Segundo, verifica-se a própria pedra colocada
    cadeia = obtem_cadeia(goban, i)

    if obtem_adjacentes_diferentes(goban,cadeia) == ():
        return remove_cadeia(goban, cadeia)
    
    return goban

def obtem_pedras_jogadores(g):
    '''
    Devolve um tuplo cujas entradas representam 
    o número de interseções ocupadas por pedras 
    brancas e pretas, respetivamente, num dado Goban.

    obtem_pedras_jogadores: goban → tuplo
    '''
    n_brancas = 0
    n_pretas = 0
    contador_lin = 0
    tamanho = obtem_lin(obtem_ultima_intersecao(g))

    while contador_lin < tamanho: # Mesmo algoritmo dos ''cria_goban...''

        while contador_lin < tamanho:

            contador_col = 0

            while contador_col < tamanho:
                    # A cada pedra preta ou branca que se encontra, aumenta-se o contador
                    if g[COLUNAS[contador_lin]][LINHAS[contador_col]] == cria_pedra_branca():
                        n_brancas += 1

                    if g[COLUNAS[contador_lin]][LINHAS[contador_col]] == cria_pedra_preta():
                        n_pretas += 1

                    contador_col += 1

            contador_lin += 1

    return (n_brancas, n_pretas)

# ---------- 2.2.1 ----------

def calcula_pontos(g):
    '''
    Devolve um tuplo cujas entradas representam 
    as pontuações dos jogadores branco e preto, 
    respetivamente, num dado Goban. 

    calcula_pontos: goban → tuple
    '''
    pontos_b = 0
    pontos_p = 0

    if eh_goban(g):
        
        n = obtem_lin(obtem_ultima_intersecao(g)) # Tamanho do Goban
        todos = obtem_territorios(g)

        for terr in todos:

            if gobans_iguais(g, cria_goban_vazio(n)): # Se o Goban estiver vazio, não verifica os territórios
                break

            verificadas = []
            fronteira = obtem_adjacentes_diferentes(g,terr)
            adicionar = True # Flag para adicionar pontos

            for inter in fronteira:

                if pedras_iguais(obtem_pedra(g, inter) ,obtem_pedra(g, fronteira[0])):
                    verificadas += [inter] # Adicona-se á lista das verificadas
                else:
                    adicionar = False # Não adiciona pontos

            if adicionar and eh_pedra_branca(g[obtem_col(verificadas[0])][obtem_lin(verificadas[0])]):
                pontos_b += len(terr) # Se a lista tiver pedras brancas, adiciona-se ás brancas

            if adicionar and eh_pedra_preta(g[obtem_col(verificadas[0])][obtem_lin(verificadas[0])]):
                pontos_p += len(terr) # Vice-versa

        # Adicionam-se também o nº de pedras de cada jogador
        pontos_b += obtem_pedras_jogadores(g)[0]
        pontos_p += obtem_pedras_jogadores(g)[1]

    return (pontos_b, pontos_p)

# ---------- 2.2.2 ----------

def eh_jogada_legal(g,i,p,l):
    '''
    Verifica se um jogada é legal (True) 
    ou não (False).

    eh_jogada_legal: goban × intersecao × pedra × goban → booleano
    '''
    # Se a interseção não for válida ou já tiver uma pedra
    if not eh_intersecao_valida(g,i) or obtem_pedra(g,i) != cria_pedra_neutra():
        return False

    copia = cria_copia_goban(g) # Cria-se uma cópia do Goban
    jogada(copia,i,p)

    if obtem_pedra(copia,i) == cria_pedra_neutra(): # Regra do suicídio
        return False
    
    return not gobans_iguais(copia,l) # Regra da repetição

# ---------- 2.2.3 ----------
'''
Defini uma função auxiliar pois iria utilizar 
a mesma verificação nas duas funções seguintes.
'''
def auxiliar_valida(g,inter,p,l):
    '''
    Função auxiliar que verifica se a 
    representação externa de uma interseção 
    é válida para uma próxima jogada, 
    num dado território.

    auxiliar_valida: goban × str x pedra × goban → booleno
    '''
    if type(inter) == str and len(inter) in (2,3): # Se tiver o tamanho válido

            if len(inter) == 2:

                if inter[1] in (chr(i) for i in range(49,58)) and \
                    inter[0] in COLUNAS:
                        
                    if eh_intersecao(str_para_intersecao(inter)) and \
                        eh_intersecao_valida(g, str_para_intersecao(inter)) and \
                            eh_jogada_legal(g, str_para_intersecao(inter), p, l):
        
                        return True

            else:

                if inter[1] in (chr(i) for i in range(49,58)) and \
                    inter[2] in (chr(i) for i in range(49,58)) and \
                        inter[0] in COLUNAS and int(inter[1:]) in LINHAS:
                            
                    if eh_intersecao(str_para_intersecao(inter)) and \
                            eh_intersecao_valida(g, str_para_intersecao(inter)) and \
                                eh_jogada_legal(g, str_para_intersecao(inter), p, l):
                        
                                return True
                
    return False
                        
def turno_jogador(g,p,l):
    '''
    Oferece ao jogador a oportunidade de 
    fazer uma jogada ou passar a sua vez.

    Para passar a sua jogada, deve introduzir 'P' 
    e a função devolverá (False).

    Para fazer uma jogada, deve introduzir uma 
    interseção válida e a função devolve (True) 
    juntamente com o Goban após a resolução jogada.

    turno_jogador: goban × pedra × goban → booleano
    '''
    while True:

        inter = str(input("Escreva uma intersecao ou 'P' para passar ["+pedra_para_str(p)+"]:"))

        if inter == 'P': # Se o jogador passar a vez, sai do loop e devolve False
            return False

        if auxiliar_valida(g,inter,p,l):
                
            jogada(g, str_para_intersecao(inter), p)
            return True

# ---------- 2.2.4 ----------

def go(n,tb,tp):
    '''
    Função principal que permite jogar um 
    jogo completo do Go de 2 jogadores.

    O jogo termina quando a jogada for 
    passada pelos 2 jogadores de seguida, 
    devolvendo se o jogador branco venceu 
    (True) ou se o preto venceu (False).

    go: int × tuple × tuple → booleano
    '''
    ib = []
    ip = []
    jogador = {
        True:cria_pedra_branca(),
        False:cria_pedra_preta() 
        }
    # Utiliza-se um dicionário com booleanos para alternar entre os jogadores
    vez = False # Começa com o jogador preto

    # Verfica-se se todos os elementos das listas são tuples e interseções válidas
    if n not in (9, 13, 19) or type(n) != int or \
        not isinstance(tb, tuple) or not isinstance(tp, tuple):
        raise ValueError('go: argumentos invalidos')

    for e in tb: # Verifica-se e converte-se as strings para interseções

        if not auxiliar_valida(cria_goban_vazio(n),e,cria_pedra_preta(),cria_goban_vazio(n)):
            raise ValueError('go: argumentos invalidos')
        ib += [str_para_intersecao(e)]
    ib = tuple(ib)

    for e in tp:

        if not auxiliar_valida(cria_goban_vazio(n),e,cria_pedra_preta(),cria_goban_vazio(n)):
            raise ValueError('go: argumentos invalidos')
        ip += [str_para_intersecao(e)]
    ip = tuple(ip)

    contador_p = 0 # Conta o número de jogadas passadas de seguida
    try:
        goban = cria_goban(n,ib,ip)
    except ValueError:
        raise ValueError('go: argumentos invalidos')

    while contador_p < 2: # Enquanto não passarem 2 vezes de seguida

        print('Branco (O) tem',(calcula_pontos(goban))[0],\
              'pontos\nPreto (X) tem',(calcula_pontos(goban))[1],'pontos')
        
        print(goban_para_str(goban))

        try:
            if not turno_jogador(goban,jogador[vez],goban):
            
                contador_p += 1

            else:
                contador_p = 0

        except ValueError:
            raise ValueError('go: argumentos invalidos')

        vez = not vez # Troca de jogador

    print('Branco (O) tem',(calcula_pontos(goban))[0],\
        'pontos\nPreto (X) tem',(calcula_pontos(goban))[1],'pontos')

    print(goban_para_str(goban))

    return (calcula_pontos(goban))[0] >= (calcula_pontos(goban))[1]

# Jogar

go(9,(),())