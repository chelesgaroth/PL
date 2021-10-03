import ply.lex as lex

tokens = ['NUM', 'PAL']
literals = ['(', ')']


def t_NUM(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_PAL(t):
    r'\w+'
    return t

t_ignore = ' \n\t'

def t_error(t):
    print('Illegal character: ' + t.value[0])

lexer = lex.lex()

'''
import sys
for line in sys.stdin:
    lexer.input(line)
    while(True):
        token = lexer.token()
        if token:
            print(token)
        else:
            break'''