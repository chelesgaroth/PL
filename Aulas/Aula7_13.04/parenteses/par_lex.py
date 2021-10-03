# Aula 7: 2021-04-13
#
#
# Linguagem dos parentesis:
# ()
# ((()))
# ()()()
# (())()((()))
#
#
# Par -> ( Par ) Par
#      | vazio
# 

import ply.lex as lex

tokens = ['PA', 'PF']

t_PA = r'\('
t_PF = r'\)'


t_ignore = " \t\n"

def t_error(t):
    print('Illegal character: ', t.value[0])
    t.lexer.skip(1)


lexer = lex.lex()