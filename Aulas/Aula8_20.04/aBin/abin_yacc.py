# (15 (7 (2 () ()) ()) (32 (25 () ()) (53 () ())))
#
# Aula 8: 2021-04-20
#
#
# ABin -> '(' num Abin Abin ')'
#       | '(' ')'
#
#

import sys
import ply.yacc as yacc

# Get the token map from the lexer.
from abin_lex import tokens

# Production rules
def p_Abin(p):
    "Abin : '(' num Abin Abin ')'"
    p[0] = "{\n\t\"root\": " + p[2] + ",\n\t\"left\": " + p[3] + ",\n\t\"right\": " + p[4] + "\n}"

def p_Abin_empty(p):
    "Abin : '(' ')'"
    p[0] = "null"


def p_error(p):
    print('Erro sintático: ', p)
    parser.success = False


# Build the parser
parser = yacc.yacc()


# Read line from input and parser it
import sys
for linha in sys.stdin:
    res = parser.parse(linha)
    print(res)
