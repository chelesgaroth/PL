import ply.yacc as yacc

from lista_compras_lex import tokens

def p_grammar(p):
    """
    lista : categorias

    categorias : categoria
               | categorias categoria

    categoria : nome ':' produtos

    nome : ID

    produtos : produto
             | produtos produto

    produto : '*' INT ';' STR ';' FLOAT ';' INT

    """

def p_error(p):
    print('Syntax Error!!')
    parser.success = False

# Build the parser
parser = yacc.yacc()


# Read input and parse it by line 

import os

cwd = os.getcwd()
      
f = open("C:\\Users\\ASUS\\Desktop\\MIEI\\3º Ano\\2º Semestre\\PL\\Aulas\\20.04\\exemploCompras.txt", "r")

content = f.read()
parser.parse(content)

f.close()
