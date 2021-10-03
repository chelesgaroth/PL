# Aula 6: 2021-04-06
#
# Converter ficheiro Latex em ficheiro HTML
#

import ply.lex as lex
import sys

# Declare your context conditions
states = (
    ('section','inclusive'),
    ('subsection','inclusive'),
    ('subsubsection','inclusive'),
    ('enumerate','inclusive'),
)

# Declare your tokens
tokens = ('SECTION', 'SUBSECTION', 'SUBSUBSECTION', 'ENUMERATE', 'OTHER')


# Rules for initial state : 0
def t_SECTION(t):
    r'\\section\{'
    print('<h1>', end='')
    t.lexer.push_state('section')

def t_SUBSECTION(t):
    r'\\subsection\{'
    print('<h2>', end='')
    t.lexer.push_state('subsection')

def t_SUBSUBSECTION(t):
    r'\\subsubsection\{'
    print('<h3>', end='')
    t.lexer.push_state('subsubsection')

def t_ENUMERATE(t):
    r'\\begin\{enumerate\}'
    print('<ol>')
    t.lexer.push_state('enumerate')

def t_OTHER(t):           
    r'.|\n'
    print(t.value, end='')


# Rules for section
def t_section_end(t):
    r'\}'
    print('</h1>')
    t.lexer.pop_state()

# Rules for subsection
def t_subsection_end(t):
    r'\}'
    print('</h2>')
    t.lexer.pop_state()

# Rules for subsubsection
def t_subsubsection_end(t):
    r'\}'
    print('</h3>')
    t.lexer.pop_state()

# Rules for enumerate
def t_enumerate_end(t):
    r'\\end\{enumerate\}'
    print('</ol>', end='')
    t.lexer.pop_state()


# Error rule for all states
def t_ANY_error(t):
    print('Illegal character: ', t.value)

#Build lexer
lexer = lex.lex()


#Reading input
f = open("example.tex", "r")


for linha in f:
    lexer.input(linha) 
    for tok in lexer:
        pass 