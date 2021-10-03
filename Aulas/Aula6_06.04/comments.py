# Aula 6: 2021-04-06
#
# Compilar comentários em C, e fazer echo do programa em si excluindo os comentários
# comments.c
#

import ply.lex as lex
import sys

states = (
    ('comentario','exclusive'), #Só o que está escrito no state comentario é que é aplicado a esse estado
)

tokens = (
    'INI', 'END', 'CONTENT'
)

# Rules for initial state: 0
def t_INI(t):
    r'/\*'
    t.lexer.begin('comentario')

def t_CONTENT(t):           #Esta regra tem de ser a última porque é um "bicho papão", apanha tudo
    r'.|\n'
    print(t.value, end='')  #end='' é para não colocar um \n por cada caracter que apanha


# Rules for comentario state
def t_comentario_END(t):
    r'\*/'
    t.lexer.begin('INITIAL')

def t_comentario_CONTENT(t):
    r'.|\n'
    t.lexer.skip(1)


# Error rule for all states
def t_ANY_error(t):
    print('Illegal character: ', t.value)



#Build lexer
lexer = lex.lex()


#Reading input
f = open("comments.c", "r")


for linha in f:
    lexer.input(linha) 
    for tok in lexer:
        pass 