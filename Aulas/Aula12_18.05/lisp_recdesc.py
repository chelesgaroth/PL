# Algoritmo recursivo descendente 
# O parser vai ter #N funções de reconhecimento + #T
'''
lisp : sexp
sexp : NUM
     | PAL
     | ( sexplist )
sexplist : 
         | sexp sexplist
'''
from ply.lex import Token
from lisp_lex import lexer


def next_symbol():
    global ps
    ps = lexer.token()

ps = None

def rec_lisp():
    if ps.type in {'NUM', 'PAL', '('}:   #lookahead
        rec_sexp()
    else:
        print(1)
        exit(1)


def rec_sexp():
    if ps.type in {'NUM'}:
        #rec_NUM()
        rec_terminal('NUM',4)
    elif ps.type in {'PAL'}:
        #rec_PAL()
        rec_terminal('PAL',5)
    elif ps.type in {'('}:
        #rec_PE()
        rec_terminal('(',6)
        rec_sexplist()
        #rec_PD()
        rec_terminal(')',7)
    else:
        print(2)
        exit(2)


def rec_sexplist():
    if ps.type in {')'}:
        pass
    elif ps.type in {'NUM', 'PAL', '('}:
        rec_sexp()
        rec_sexplist()
    else:
        print(3)
        exit(3)

def rec_terminal(t, error):
    if ps.type == t:
        next_symbol()
    else:
        print(error)
        exit(error)



import sys

for line in sys.stdin:
    lexer.input(line)
    ps = lexer.token()
    rec_lisp()



#def rec_NUM():
#    if ps == 'NUM':
#        ps = next_symbol()
#    else:
#        exit(4)
#
#def rec_PAL():
#    pass
#
#def rec_PE():
 #   pass
#
#def rec_PD():
#    pass
