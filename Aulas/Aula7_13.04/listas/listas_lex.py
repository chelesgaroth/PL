# listas-yacc.py
# Aula 7: 2021-04-13
# Listas heterogéneos: inteiros e alfanuméricos
#
#
#
#
#

import ply.lex as lex

tokens = ['PA', 'PF', 'VIRG', 'number', 'alfanum']

t_PA = r'\['
t_PF = r'\]'
t_VIRG = r','
t_number = r'\d+'
t_alfanum = r'[a-zA-Z](\w|\d)*'

t_ignore = " \t\n"

def t_error(t):
    print('Illegal character: ', t.value[0])
    t.lexer.skip(1)


lexer = lex.lex()



