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

import ply.yacc as yacc
from par_lex import tokens

# Production rules
def p_axioma(p):
    "S : Par"
    pass

def p_parentesis(p):
    "Par : PA Par PF Par"
    pass

def p_parentesis_empty(p):
    "Par : "
    pass

def p_error(p):
    print('Erro sintático: ', p)
    parser.success = False


# Build the parser
parser = yacc.yacc()


# Read line from input and parser it
import sys
for linha in sys.stdin:
    parser.success = True
    res = parser.parse(linha)
    if parser.success:
        print("Frase válida ", linha)
    else:
        print("Frase inválida... Corrija and try again.")