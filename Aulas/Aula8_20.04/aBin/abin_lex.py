# (15 (7 (2 () ()) ()) (32 (25 () ()) (53 () ())))
#
# Aula 8: 2021-04-20
#
#
# ABin -> '(' num Abin Abin ')'
#       | '(' ')'
#
#
#

import ply.lex as lex

tokens = ['num']
literals = ['(', ')'] # em vez de usar PA e PF e não preciso de definir t


t_num = r'(\+|-)?\d+'


t_ignore = " \t\n"

def t_error(t):
    print('Illegal character: ', t.value[0])
    t.lexer.skip(1)


lexer = lex.lex()

