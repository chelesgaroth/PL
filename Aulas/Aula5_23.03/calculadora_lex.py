# aula4 : 2021-03-23
#
# É um tokenizer
#
#

import ply.lex as lex
import sys

#List of token names
tokens = (
    'PA', 'PF',
    'ADD', 'SUB',
    'MUL', 'DIV',
    'NUM'
)


#Regex for tokens
t_PA = r'\('
t_PF = r'\)'
t_ADD = r'\+'
t_SUB = r'-'
t_MUL = r'\*'
t_DIV = r'\/'
# t_NUM = r'\d+' Quando quero definir mais alguma tenho de fazer uma função


#Regex with action code
def t_NUM(t):
    r'\d+'
    t.value = int(t.value) #queremos passar para inteiro
    return t               #devemos sempre fazer return


#Controlling line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


#Ignore things
t_ignore = " \t" #ou "\s+"


#Errors 
def t_error(t):
    print('Illegal character: ' + t.value[0]) # ou (f"Illegal character {t.value[0]}")
    t.lexer.skip(1)


#Build lexer
lexer = lex.lex()

#Reading input
for linha in sys.stdin:
    lexer.input(linha)
    for tok in lexer:
        print(tok)
        #pass sou obrigado a percorrer todos os tokens nem que não faça nada 
