import ply.lex as lex

tokens = ['NUM','id']
literals = ['+', '-', '*', '/', '(', ')','!','?','$','=']

def t_NUM(t):
    r'\d+'
    t.value = int(t.value)
    return t

t_id = r'\w+'

t_ignore = " \t\n"

def t_error(t):
    print('Illegal character: ', t.value[0])
    t.lexer.skip(1)


lexer = lex.lex()