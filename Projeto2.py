# 86400 Daniel dos Santos Fernandes

#------------------------#
#Tipos abstratos de Dados#
#------------------------#

#--Tipo Posicao--#
#representacao: tuplo-> (linha, coluna)

#construtor
def faz_pos(l,c):
    if isinstance(l, int) and isinstance(c, int) and 0<=l and 0<=c:
        return (l,c)
    else:
        raise ValueError('faz_pos: argumentos errados')
    
#seletores
def linha_pos(p):
    return p[0]

def coluna_pos(p):
    return p[1]

#reconhecedor
def e_pos(arg):
    return isinstance(arg, tuple) and len(arg)==2 and isinstance(arg[0], int) and isinstance(arg[1], int) and 0<=arg[0] and 0<=arg[1]

#teste
def pos_iguais(p1, p2):
    return p1==p2

#--Tipo Chave--#
#representacao: tuplo de tuplos (os tuplos internos correspondem as diferentes linhas)

#construtores
def gera_chave_linhas(l, mgc):
    chave_aux=()
    if verifica_l(l) and verifica_mgc(mgc):
        for e in mgc:
            if e in l and e not in chave_aux:       #forma um tuplo com as letras da mgc sem repeticoes e sem espacos
                chave_aux=chave_aux+tuple(e)
        for f in l:                                 #junta as restantes letras ao tuplo
            if f not in chave_aux:                      
                chave_aux=chave_aux+tuple(f)
        return (chave_aux[0:5], chave_aux[5:10], chave_aux[10:15], chave_aux[15:20], chave_aux[20:25])
    else:
        raise ValueError('gera_chave_linhas: argumentos errados')
    
def gera_chave_espiral(l, mgc, s, pos):
    if verifica_l(l) and verifica_mgc(mgc) and (s=='r' or s=='c') and (pos==(0,0) or pos==(0,4) or pos==(4,0) or pos==(4,4)):
        lst_pos=posicoes(s, pos)                #retorna uma lista com as posicoes que devem ser tomadas pelas letras
        dicio_pos={}
        mgc_aux=''
        chave_aux=()
        for e in mgc:                           #remove os espacos
            if e not in mgc_aux and e in l:
                mgc_aux=mgc_aux+e
        for f in l:                             #junta as restantes letras
            if f not in mgc_aux:
                mgc_aux=mgc_aux+f
        for i in range(0, len(mgc_aux)):        #forma um dicionario, cada chave eh uma posicao e o elemento dessa chave eh a letra que vai tomar essa posicao
            dicio_pos[lst_pos[i]]=mgc_aux[i]
        for l in range(0, 5):                   #forma um tuplo a partir do dicionario
            for c in range(0, 5):
                chave_aux=chave_aux+tuple(dicio_pos[(l,c)])
        return (chave_aux[0:5], chave_aux[5:10], chave_aux[10:15], chave_aux[15:20], chave_aux[20:25])
    else:
        raise ValueError('gera_chave_espiral: argumentos errados')
            
        
#auxiliares de construtores
def verifica_mgc(mgc):
    L=('A','B','C','D','E','F','G','H','I','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',' ')
    mgc_novo=''
    if isinstance(mgc, str):
        for e in mgc:
            if e in L:
                mgc_novo=mgc_novo+str(e)
        if mgc_novo==mgc:
            return True
        else:
            return False
    else:
        return False
    
def verifica_l(l):
    Letras=('A','B','C','D','E','F','G','H','I','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z')
    l_novo=()
    if len(l)==25:
        for e in l:
            if e in Letras and e not in l_novo:
                l_novo=l_novo+tuple(e)
        if len(l_novo)==len(l):
            return True
        else:
            return False
    else:
        return False
    
#operacoes para funcao posicoes------------------
op1 = lambda x: (linha_pos(x), coluna_pos(x)+1)
op2 = lambda x: (linha_pos(x)+1, coluna_pos(x))
op3 = lambda x: (linha_pos(x), coluna_pos(x)-1)
op4 = lambda x: (linha_pos(x)-1, coluna_pos(x))
#------------------------------------------------
def posicoes(s, pos):   
    lst_pos=[pos]
    if s=='r':                  #determina a primeira direcao da espiral
        if pos==(0,0):
            op=op1
        elif pos==(0,4):
            op=op2
        elif pos==(4,4):
            op=op3
        elif pos==(4,0):
            op=op4
    else:
        if pos==(0,0):
            op=op2
        elif pos==(0,4):
            op=op3
        elif pos==(4,4):
            op=op4
        elif pos==(4,0):
            op=op1
    pos=op(pos)
    lst_pos=lst_pos+[pos]    
    while pos!=(2,2):
        if pos!=(0,0) and pos!=(0,4) and pos!=(4,0) and pos!=(4,4) and op(pos) not in lst_pos:  #verifica se nao chegou a um limite
            pos=op(pos)
            lst_pos=lst_pos+[pos]
        else:                                                                                   #caso contrario muda a direcao
            op=muda_operacao(op, s)
            pos=op(pos)
            lst_pos=lst_pos+[pos]
    return lst_pos

def muda_operacao(op, s): 
    if s=='r':
        if op==op1:
            op=op2
        elif op==op2:
            op=op3
        elif op==op3:
            op=op4
        else:
            op=op1
    else:
        if op==op1:
            op=op4
        elif op==op2:
            op=op1
        elif op==op3:
            op=op2
        else:
            op=op3
    return op

#seletor
def ref_chave(c,p):
    return c[linha_pos(p)][coluna_pos(p)]

#modificador    
def muda_chave(c, p, l):
    c=c[:linha_pos(p)]+(c[linha_pos(p)][:coluna_pos(p)]+tuple(l)+c[linha_pos(p)][coluna_pos(p)+1:],)+c[linha_pos(p)+1:]
    return c
    

#reconhecedor
def e_chave(arg):
    L=('A','B','C','D','E','F','G','H','I','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z')
    letras=[]
    if isinstance(arg, tuple) and len(arg)==5:
        for l in arg:
            if isinstance(l, tuple) and len(l)==5:
                for c in l:
                    if isinstance(c, str) and c in L and c not in letras:
                        letras=letras+[c]
                        
                    else:
                        return False
            else:
                return False
        return True
    else:
        return False
    
#transformador
def string_chave(c):
    tab=''
    for col in c:
        for lin in col:
            tab=tab+str(lin)+' '
        tab=tab+'\n'
    return tab
            
            
#------------------#
#Funcoes principais#
#------------------#

def digramas(mens):
    dig=''
    j=0
    for i in range(len(mens)):              #retira os espacos
        if mens[i]!=' ':
            dig=dig+mens[i]
    while j<len(dig)-1:                     #troca a segunda letra dos digramas com letras iguais por X
        if dig[j]==dig[j+1] and j%2==0:
            dig=dig[:j+1]+'X'+dig[j+1:]
            j=0
        else:
            j=j+1     
    if len(dig)%2!=0:                       #adiciona um X no final caso seja um numero impar de letras
        dig=dig+'X'
    return dig

def figura(digrm, chave):
    for l in range(5):                      #percorre a chave
        for c in range(5):
            if digrm[0]==chave[l][c]:       #acha a posicao das letras do digrama na chave
                pos1=faz_pos(l,c)
            if digrm[1]==chave[l][c]:
                pos2=faz_pos(l,c)
    if linha_pos(pos1)==linha_pos(pos2):
        fig='l'
    elif coluna_pos(pos1)==coluna_pos(pos2):
        fig='c'
    else:
        fig='r'
    return (fig, pos1, pos2)

def codifica_l(pos1, pos2, inc):
    if inc==1:
        if coluna_pos(pos1)==4:                                     #se a posicao tiver na coluna 4 volta a coluna 0
            pos1_cod=faz_pos(linha_pos(pos1), 0)
        else:                                                       #caso contrario soma 1 a coluna (similar para o resto da funcao)
            pos1_cod=faz_pos(linha_pos(pos1), coluna_pos(pos1)+1)
        if coluna_pos(pos2)==4:
            pos2_cod=faz_pos(linha_pos(pos2), 0)
        else:
            pos2_cod=faz_pos(linha_pos(pos2), coluna_pos(pos2)+1)
    else:
        if coluna_pos(pos1)==0:
            pos1_cod=faz_pos(linha_pos(pos1), 4)
        else:
            pos1_cod=faz_pos(linha_pos(pos1), coluna_pos(pos1)-1)
        if coluna_pos(pos2)==0:
            pos2_cod=faz_pos(linha_pos(pos2), 4)
        else:
            pos2_cod=faz_pos(linha_pos(pos2), coluna_pos(pos2)-1)
    return (pos1_cod, pos2_cod)

def codifica_c(pos1, pos2, inc):
    if inc==1:
        if linha_pos(pos1)==4:                                      #se a posicao tiver na linha 4 volta a linha 0
            pos1_cod=faz_pos(0, coluna_pos(pos1))
        else:                                                       #caso contrario soma 1 a linha (similar para o resto da funcao)
            pos1_cod=faz_pos(linha_pos(pos1)+1, coluna_pos(pos1))
        if linha_pos(pos2)==4:
            pos2_cod=faz_pos(0, coluna_pos(pos2))
        else:
            pos2_cod=faz_pos(linha_pos(pos2)+1, coluna_pos(pos2))
    else:
        if linha_pos(pos1)==0:
            pos1_cod=faz_pos(4, coluna_pos(pos1))
        else:
            pos1_cod=faz_pos(linha_pos(pos1)-1, coluna_pos(pos1))
        if linha_pos(pos2)==0:
            pos2_cod=faz_pos(4, coluna_pos(pos2))
        else:
            pos2_cod=faz_pos(linha_pos(pos2)-1, coluna_pos(pos2))
    return (pos1_cod, pos2_cod)
    

def codifica_r(pos1, pos2):
    pos1_cod=faz_pos(linha_pos(pos1), coluna_pos(pos2))         #troca a coluna das duas posicoes
    pos2_cod=faz_pos(linha_pos(pos2), coluna_pos(pos1))
    return (pos1_cod, pos2_cod)

def codifica_digrama(digrm, chave, inc):
    f=figura(digrm, chave)               #devolve (fig, pos1, pos2)
    if f[0]=='l':
        pos=codifica_l(f[1], f[2], inc)  #devolve (pos1_cod, pos2_cod)
    elif f[0]=='c':
        pos=codifica_c(f[1], f[2], inc)  #devolve (pos1_cod, pos2_cod)
    else:
        pos=codifica_r(f[1], f[2])       #devolve (pos1_cod, pos2_cod)
    
    return ref_chave(chave, pos[0])+ref_chave(chave, pos[1])

def codifica(mens, chave, inc):
    dig=digramas(mens)
    cod=''
    for i in range(0, len(dig), 2):
        cod=cod+codifica_digrama(dig[i:i+2], chave, inc)
    return cod
    