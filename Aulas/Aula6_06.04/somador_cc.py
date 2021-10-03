# Aula6: 2021-04-06
#
# Somador on/off com condições de contexto
#    - semáforo está on de início
#    - lê do input
#    - reagir a estímulos:
#           r'[oO][nN]' --> ligar o semáforo
#           r'(o|O)(n|N)'
#           r'[oO][fF]{2}' --> desligar o semáforo
#           r'(o|O)(f|F)(f|F)'
#           r'='  --> escrever o valor acumulado
#           r'\d+' --> acrescentar o valor lido ao acumulado se semáforo ligado
#           qq outra coisa --> descartar

import ply.lex as lex
import sys

#Declare your context conditions
states = (
    ('semaforo','inclusive'),
)

#Declare your tokens
tokens = ('ON', 'OFF', 'PRINT', 'NUMBER')

#Rules for initial state: 0  => O semáforo está ligado neste estado 0
def t_OFF(t):
    r'[Oo][fF]{2}'
    t.lexer.begin('semaforo') #Vai para o desligado - semaforo

def t_NUMBER(t):
    r'\d+'
    t.lexer.soma = t.lexer.soma + int(t.value)

def t_PRINT(t):
    r'='
    print("Soma = ",t.lexer.soma)

#Não vamos definir o on porque ele vai estar no outro estado possivel


#Ignore things
t_ignore = " \t" #ou "\s+"

#Errors 
def t_error(t):
    #print('Illegal character: ' + t.value[0]) # ou (f"Illegal character {t.value[0]}") 
    t.lexer.skip(1)


#Rules for semaforo state:   => O semáforo está desligado neste estado 'semaforo'
def t_semaforo_ON(t):
    r'[oO][nN]'
    t.lexer.begin('INITIAL') #Volta ao 0 - ligado

def t_semaforo_NUMBER(t):
    r'\d+'
    t.lexer.skip(len(t.value))


#Build lexer
lexer = lex.lex()

#My state
lexer.soma = 0

#Reading input
for linha in sys.stdin:
    lexer.input(linha) 
    for tok in lexer:
        pass 
       