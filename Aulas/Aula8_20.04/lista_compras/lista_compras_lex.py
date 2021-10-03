import ply.lex as lex

tokens = [
    'ID',
    'FLOAT',
    'INT',
    'STR'
]

literals = [':',';','*']

t_ID =r'\w+'
# t_STR = r'\"[^\"]+\"'


def t_STR(t):
    r'\"[^\"]+\"'
    t.value = t.value[1:-1] # apanha tudo desde a posição até as anteriores todas, isto é -1 [1,-1[
    return t


def t_FLOAT(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return  t


def t_INT(t):
    r'\d+'
    t.value = int(t.value)
    return t

t_ignore = ' \n\t' 

def t_error(t):
    print('Illegal character: ' + t.value[0])
    t.lexer.skip(1) #é para não parar, continuar a correr e apresentar me os erros todos que encontrou

lexer = lex.lex()

