# aula4 : 2021-03-23
#
# É um tokenizer
#
#

import ply.lex as lex
import sys

#List of token names
tokens = (
    'ON', 'OFF',
    'DIG', 'EQ'
)


#Regex with action code
def t_ON(t):
    r'[oO][nN]'
    t.lexer.semaforo = True

def t_OFF(t):
    r'[oO][fF]{2}'
    t.lexer.semaforo = False

def t_EQ(t):
    r'='
    print("Soma = ", t.lexer.soma)

def t_DIG(t):
    r'\d+'
    if t.lexer.semaforo:
        t.lexer.soma += int(t.value)


#Controlling line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


#Ignore things
t_ignore = " \t" #ou "\s+"


#Errors 
def t_error(t):
    #print('Illegal character: ' + t.value[0]) # ou (f"Illegal character {t.value[0]}") 
    # Desta forma ignora os erros
    t.lexer.skip(1)


#Build lexer
lexer = lex.lex()

#My state
lexer.semaforo = True
lexer.soma = 0

#Reading input
for linha in sys.stdin:
    lexer.input(linha) # o lexer pega na linha e parte em vários tokens, para cada token reage com a ação que definimos para cada
    for tok in lexer:
        #print(tok)
        pass 
        # Sou obrigado a percorrer todos os tokens nem que não faça nada 
