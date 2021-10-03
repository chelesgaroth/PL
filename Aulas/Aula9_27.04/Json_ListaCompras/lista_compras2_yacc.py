import ply.yacc as yacc
from lista_compras_lex import tokens

#Construir ficheiro Json

def p_lista(p):
    "lista : categorias"
    print('{' + p[1] + '}')

def p_categorias_categoria(p):
    "categorias : categoria"
    p[0] = p[1]

def p_categorias_categorias(p):
    "categorias : categorias categoria"
    p[0] = p[1] + ', ' + p[2]

def p_categoria(p):
    "categoria : nome ':' produtos"
    p[0] = f'"{p[1]}" : [ {p[3]} ]'

def p_nome(p):
    "nome : id"
    p[0] = p[1]

def p_produtos_produto(p):
    "produtos : produto"
    p[0] = p[1]

def p_produtos_produtos(p):
    "produtos : produtos produto"
    p[0] = p[1] + ', ' + p[2]

def p_produto(p):
    "produto : '*' INT ';' STR ';' FLOAT ';' INT"
    p[0] =f'{{ "id": {p[2]},\n "nome": {p[4]},\n "preco": {p[6]},\n "quantidade":{p[8]}}}'


def p_error(p):
    print('Syntax Error!!')
    parser.success = False

# Build the parser
parser = yacc.yacc()


# Read input and parse it by line 
import os

cwd = os.getcwd()
      
f = open("exemploCompras.txt", "r")

content = f.read()
parser.parse(content)

f.close()
