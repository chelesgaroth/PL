# listas-yacc.py
# Aula 7: 2021-04-13
# Listas heterogéneos: inteiros e alfanuméricos
#   []
#   [78]
#   [1, 2, 3]
#   [a, barco]
#   [121, asa, c45]
#
# Listas --> '[' ']'
#          | '[' Elementos ']'
#
# Elementos --> Elementos ',' Elemento
#             | Elemento
#
# Elemento --> number
#            | alfanum
#
#
#

import ply.yacc as yacc
from listas_lex import tokens

def p_grammar(p):
    """

    Lista : PA Elementos PF
          | PA PF

    Elementos : Elementos VIRG Elemento
              | Elemento 

    Elemento : number
             | alfanum
    
    """

def p_error(p):
    print('Erro sintático: ', p)
    parser.success = False


# Build the parser
parser = yacc.yacc()


# Read line from input and parser it
import sys
for linha in sys.stdin:
    parser.success = True
    parser.parse(linha)
    if parser.success:
        print("Frase válida")
    else:
        print("Frase inválida... Corrija and try again.")