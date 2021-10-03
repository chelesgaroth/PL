import sys
import ply.yacc as yacc

from mistas_lex import tokens


def p_lista(p):
    "lista : LPAREN elementos RPAREN"
    pass


def p_elementos_virg(p):
    "elementos : elementos VIRG elemento"   #Ao utilizarmos o yacc é muito mais aconselhável usar a recursividade à esquerda
    #p.parser.elements += 1
    print(p[1])
    p[0] = [p[1]] + p[3]                   #Neste caso estamos usar recursividade à direita, não faz muito diferença porque é um exemplo pequeno
    #p[0] = p[1] + [p[3]]                   #Aqui já usamos recursividade à esquerda

def p_conteudo_elementos(p):
    "conteudo : elementos"
    p[0] = p[1]

def p_elementos_elemento(p):
    "elementos : elemento"
    p.parser.elements = 1
    #p[0] = [p[1]]

def p_elemento_id(p):
    "elemento : ID"
    p.parser.words.append(p[1])
    #p[0] = p[1]


def p_elemento_num(p):
    "elemento : NUM"
    p.parser.numbers.append(p[1])
    p.parser.sum += p[1]
    #p[0] = p[1]
    


def p_error(p):
    print('Syntax error!')
    parser.success = False


parser = yacc.yacc()

for line in sys.stdin:
    parser.success = True
    parser.numbers = []
    parser.words = []
    parser.elements = 0
    parser.sum = 0

    parser.parse(line)

    if parser.success:
        print('Parsing completed!')
        print('Elements:', parser.elements)
        print('Numbers - quantity: ', len(parser.numbers), ' values: ', parser.numbers, ' sum: ', parser.sum)
        print('Words:', parser.words)



