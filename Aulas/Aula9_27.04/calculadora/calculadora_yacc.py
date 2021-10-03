import ply.yacc as yacc
from calculadora_lex import tokens


def p_calculadora(p):
    "calculadora : comandos"

def p_comandos(p):
    """
    comandos : comando comandos
             |
    """

def p_comando_declaracao(p): #inicializa uma variável a 0
    "comando : '$' id"
    p.parser.variaveis[p[2]] = 0 #p.parser.variaveis.update({p[2]: 0})

def p_comando_leitura(p):
    "comando : '?' id"
    v =input('Introduza um valor inteiro: ')
    p.parser.variaveis[p[2]] = int(v)

def p_comando_escrita(p):
    "comando : '!' expressao"
    print(p[2])

def p_comando_atribuicao(p):
    "comando : id '=' expressao"
    p.parser.variaveis[p[1]] = p[3]

def p_comando_informacao(p):
    "comando : '!' '!'"
    print(p.parser.variaveis)

def p_expressao_mais(p):
    "expressao : expressao '+' termo"
    p[0] = p[1] + p[3]

def p_expressao_menos(p):
    "expressao : expressao '-' termo"
    p[0] = p[1] - p[3]

def p_expressao_termo(p):
    "expressao : termo"
    p[0] = p[1]

def p_termo_multi(p):
    "termo : termo '*' fator"
    p[0] = p[1] * p[3]

def p_termo_div(p):
    "termo : termo '/' fator"
    p[0] = p[1] // p[3]

def p_termo_fator(p):
    "termo : fator"
    p[0] = p[1]

def p_fator_id(p):
    "fator : id"
    if p[1] not in p.parser.variaveis:
        print(f"WARNING. Variável não declarada: '{p[1]}'. Vou inicializar a variável a 0. ")
        p.parser.variaveis[p[1]] = 0
    p[0] = p[1]

def p_fator_num(p):
    "fator : NUM"
    p[0] = p[1]

def p_fator_expressao(p):
    "fator : '(' expressao ')'"
    p[0] = p[2]


def p_error(p):
    print('Erro sintático: ', p)
    parser.success = False


# Build the parser
parser = yacc.yacc()
parser.variaveis = {}


# Read line from input and parser it
import sys
for linha in sys.stdin:
    res = parser.parse(linha)
    #print(res)