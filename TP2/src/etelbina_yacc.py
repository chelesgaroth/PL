import ply.yacc as yacc
from etelbina_lex import tokens


def p_Aplicacao(p):
    "Aplicacao : Declaracoes Content"
    global fwrite 
    fwrite.write(f"{p[1]}{p[2]}")

def p_Content(p):
    "Content : function Instrucoes end"
    p[0] = "start\n" + str(p[2]) + "stop\n"

def p_Declaracoes(p):
    " Declaracoes : Declaracao '.' Declaracoes"
    p[0] = p[1] + p[3]

def p_DeclaracoesEmpty(p):
    "Declaracoes : "
    p[0] = ""

def p_Declaracao(p):
    "Declaracao : int var"
    if p[2] in p.parser.variaveis:
        p[0] = f"err \"ERROR. Variavel ja declarada:\"\n"
        print(f"ERROR. Variável já declarada:'{p[2]}'")
        parser.success = False
    else:
        p.parser.variaveis[p[2]] = ["int",p.parser.sp]
        p[0]=("pushi 0\n")
        p.parser.sp+=1

def p_Declaracao_Array(p):
    "Declaracao : int var '[' num ']'"
    if p[2] in p.parser.variaveis:
        p[0] = f"err \"ERROR. Variavel ja declarada:\"\n"
        print(f"ERROR. Variável já declarada:'{p[2]}'")
        parser.success = False
    else:
        p[0]=(f"pushn {int(p[4])}\n")
        p.parser.variaveis[p[2]] = ["array",int(p[4]),p.parser.sp]
        p.parser.sp+=int(p[4])

def p_Declaracao_DoubleArray(p):
    "Declaracao : int var '[' num ']' '[' num ']'"
    if p[2] in p.parser.variaveis:
        p[0] = f"err \"ERROR. Variavel ja declarada:\"\n"
        print(f"ERROR. Variável já declarada:'{p[2]}'")
        parser.success = False
    else:
        p[0]=(f"pushn {(int(p[4])*int(p[7]))}\n")
        p.parser.variaveis[p[2]] = ["array",(int(p[4])*int(p[7])),int(p[4]),int(p[7]),p.parser.sp] 
        p.parser.sp+=(int(p[4])*int(p[7]))


def p_Declaracao_atribuicao(p):
    "Declaracao : int var '=' NumNP"
    if p[2] in p.parser.variaveis:
        p[0] = f"err \"ERROR. Variavel ja declarada:\"\n"
        print(f"ERROR. Variável já declarada:'{p[2]}'")
        parser.success = False
    else:
        p.parser.variaveis[p[2]] = ["int",p.parser.sp]
        p[0]= p[4]
        p.parser.sp+=1

def p_Declaracao_Array_Atribuicao(p):
    "Declaracao : int var '[' num ']' '=' '{' Array '}'"
    if p[2] in p.parser.variaveis:
        p[0] = f"err \"ERROR. Variavel ja declarada:\"\n"
        print(f"ERROR. Variável já declarada:'{p[2]}'")
        parser.success = False
    else:
        p[0] = p[8]
        if p.parser.elemsCount == int(p[4]):
            p.parser.variaveis[p[2]] = ["array",int(p[4]),p.parser.sp]
            p.parser.sp+=int(p[4])
        else:
            p[0] = f"err \"ERROR. Elementos do array nao coincide com a declaracao\"\n"
            print(f"ERROR. Elementos do array nao coincide com a declaracao'{p[2]}'")
            parser.success = False
    p.parser.elemsCount = 0


def p_Declaracao_DoubleArray_Atribuicao(p):
    "Declaracao : int var '[' num ']' '[' num ']' '=' '{' DoubleArray '}'"
    if p[2] in p.parser.variaveis:
        p[0] = f"err \"ERROR. Variavel ja declarada:\"\n"
        print(f"ERROR. Variável já declarada:'{p[2]}'")
        parser.success = False
    else:
        p[0] = p[11]
        i = int(p[4])
        j = int(p[7])
        if (i==p.parser.elems2Count)and(j==p.parser.colCount)and(i*j==p.parser.elemsCount):
            p.parser.variaveis[p[2]] = ["array",i*j,i,j,p.parser.sp]
            p.parser.sp+=(i*j)
        else:
            p[0] = f"err \"ERROR. Elementos do array nao coincide com a declaracao\"\n"
            print(f"ERROR. Elementos do array nao coincide com a declaracao'{p[2]}'")
            parser.success = False
    p.parser.elemsCount = 0
    p.parser.elems2Count = 0
    p.parser.bool = 1


# ------------------ ARRAY/DOUBLE-ARRAY --------------------------

def p_DoubleArray(p):
    "DoubleArray : '{' Array '}' ElemsDArray"
    p[0] = p[2] + p[4]
    p.parser.elems2Count +=1 #conta as linhas

def p_ElemsDArray(p):
    "ElemsDArray : ',' '{' Array '}' ElemsDArray "
    p[0] = p[3] + p[5]
    p.parser.elems2Count +=1  #conta as linhas

def p_ElemsDArrayEmpty(p):
    "ElemsDArray : "
    p[0] = ""

def p_Array(p):
    "Array : NumNP Elems"
    p[0] = p[1] + p[2]
    p.parser.elemsCount +=1 #conta o número de elementos no total do array
    if(p.parser.bool==1):
        p.parser.colCount = p.parser.elemsCount #conta as colunas
        p.parser.bool=0

def p_Elems(p):
    "Elems : ',' NumNP Elems"
    p[0] = p[2] + p[3]
    p.parser.elemsCount +=1

def p_Elems_Empty(p):
    "Elems : "
    p[0] = ""
    
    



# ----------------- INSTRUCOES ----------------------
def p_Instrucoes(p):
    "Instrucoes : Instrucao '.' Instrucoes"
    p[0] = p[1] + p[3]

def p_Instrucoes_Empty(p):
    "Instrucoes : "
    p[0] = ""

# ----------------- INSTRUÇÃO -------------------------

def p_Instrucao_Loop(p):
    "Instrucao : Loop"
    p[0] = p[1]

def p_Instrucao_Condition(p):
    "Instrucao : Condition"
    p[0]=(f"{p[1]}")


def p_Instrucao_Print(p):
    "Instrucao : Print"
    p[0]=(f"{p[1]}")
    

def p_Instrucao_Read(p):
    "Instrucao : VarArray '=' read "
    if(len(p[1])==3):
        p[0] =  p[1][0] + p[1][1] + (f"read\natoi\n") + "storen\n"
    else :
        p[0] = (f"read\natoi\n") + p[1][0]
        

def p_Instrucao_Expressao(p):
    "Instrucao : VarArray '=' Expressao"
    if(len(p[1])==3):
        p[0] = p[1][0] + p[1][1] + p[3] + p[1][2]
    else :
        p[0] = p[3] + p[1][0]

def p_Instrucao_MaisMais(p):
    "Instrucao : VarArray inc"
    if(len(p[1])==3):
        p[0] = p[1][0] + p[1][1] + p[1][0] + p[1][1] + "loadn\n" + "pushi 1\nadd\n" + p[1][2]
    else :
        p[0] = p[1][1] + "pushi 1\nadd\n" + p[1][0]


def p_Instrucao_MenosMenos(p):
    "Instrucao : VarArray dec"
    if(len(p[1])==3):
        p[0] = p[1][0] + p[1][1] + p[1][0] + p[1][1] + "loadn\n" + "pushi 1\nsub\n" + p[1][2] #carrega para a stack o ender-base, depois vai buscar o valor e aumenta 1 valor
    else :
        p[0] = p[1][1] + "pushi 1\nsub\n" + p[1][0]

# ----------------- LOOP ---------------------------
def p_Loop(p):
    "Loop : repeat '{' Instrucoes '}' until Verifica"
    p[0] = f"repeat{p.parser.loopCount}:\n{p[3]}{p[6]}jz repeat{p.parser.loopCount}\n"
    p.parser.loopCount +=1


#----------------IF ELSE------------------------

def p_Condition(p):
    "Condition : if Verifica '{' Instrucoes '}' "
    p[0] = f"{p[2]}jz if{p.parser.labelCount}\n{p[4]}if{p.parser.labelCount}:\n"
    p.parser.labelCount+=1
    

def p_Condition_else(p):
    "Condition : if Verifica '{' Instrucoes '}' else '{' Instrucoes	'}' "
    p[0] = f"{p[2]}jz if{p.parser.labelCount}\n{p[4]}jump ifend{parser.labelCount}\nif{p.parser.labelCount}:\n{p[8]}ifend{parser.labelCount}:\n"

    

#-------------------- VERIFICA ----------------------
def p_Verifica_cond(p):
    "Verifica : '(' Cond ')' "
    p[0] = p[2]

def p_Verifica_naocond(p):
    "Verifica : '!' '(' Cond ')' "
    p[0] = f"{p[3]}not\n"

def p_Verifica_And(p):
    "Verifica : Verifica and Verifica"
    p[0] = f"{p[1]}{p[3]}mul\n"

def p_Verifica_Or(p):
    "Verifica : Verifica or Verifica"
    p[0] = f"{p[1]}{p[3]}add\n{p[1]}{p[3]}mul\nsub\n"


# ----------------- COND ----------------------------
def p_Cond_Equals(p):
    "Cond : Expressao equals Expressao"
    p[0] = f"{p[1]}{p[3]}equal\n"

def p_Cond_LessEq(p):
    "Cond : Expressao lessEq Expressao"
    p[0] = f"{p[1]}{p[3]}infeq\n"

def p_Cond_MoreEq(p):
    "Cond : Expressao moreEq Expressao"
    p[0] = f"{p[1]}{p[3]}supeq\n"

def p_Cond_Menor(p):
    "Cond : Expressao '<' Expressao"
    p[0] = f"{p[1]}{p[3]}inf\n"

def p_Cond_Maior(p):
    "Cond : Expressao '>' Expressao"
    p[0] = f"{p[1]}{p[3]}sup\n"

def p_Cond_Verifica(p):
    "Cond : Verifica"
    p[0] = p[1]


#------------------- PRINT -----------------------------
def p_Print_VarArray(p):
    "Print : print VarArray"
    if(len(p[2])==3):
        p[0] = p[2][0]  + p[2][1] + "loadn\n" +"writei\n"
    else :
        p[0] = p[2][1] +"writei\n"


def p_Print_string(p):
    "Print : print string"
    p[0] = f"pushs {p[2]}\nwrites\n"



#------------------------ EXPRESSAO -------------------------

def p_Expressao_mais(p):
    "Expressao : Expressao '+' Termo"
    p[0] = p[1] + p[3] + "add\n"

def p_Expressao_menos(p):
    "Expressao : Expressao '-' Termo"
    p[0] = p[1] + p[3] + "sub\n"

def p_Expressao_Termo(p):
    "Expressao : Termo"
    p[0] = p[1]

def p_Termo_multi(p):
    "Termo : Termo '*' Fator"
    p[0] = p[1] + p[3] + "mul\n"
  
def p_Termo_div(p):
    "Termo : Termo '/' Fator"
    p[0] = p[1] + p[3] + "div\n"

def p_Termo_fator(p):
    "Termo : Fator"
    p[0] = p[1]
  
def p_Fator_VarN(p):
    "Fator : NumNP"
    p[0]=p[1]

def p_Fator_VarArray(p):
    "Fator : VarArray"
    if(len(p[1])==3): #Array
        p[0] = p[1][0] + p[1][1] + "loadn\n"
    else : #Variável
        p[0] = p[1][1]

def p_Fator_expressao(p):
    "Fator : '(' Expressao ')' "
    p[0] = p[2]


def p_NumNP_NumNeg(p):
    "NumNP : numNeg"
    p[0] = f"pushi {p[1]}\n"

def p_NumNP_Num(p):
    "NumNP : num"
    p[0] = f"pushi {p[1]}\n"


def p_VarArray_array(p):
    "VarArray : var '[' Expressao ']'"
    if p[1] not in p.parser.variaveis:
        p[0] = f"err \"ERROR. Variavel nao declarada:\"\n"
        print(f"ERROR. Variavel nao declarada:'{p[1]}'")
        parser.success = False
    else:
        p[0] = (f"pushgp\npushi {p.parser.variaveis[p[1]][2]}\npadd\n" , p[3] , "storen\n")



def p_VarArray_double_array(p):
    "VarArray : var '[' Expressao ']' '[' Expressao ']'"
    if p[1] not in p.parser.variaveis:
        p[0] = f"err \"ERROR. Variavel nao declarada:\"\n"
        print(f"ERROR. Variavel nao declarada:'{p[1]}'")
        parser.success = False
    else:
        col = p.parser.variaveis[p[1]][3]
        p[0] = (f"pushgp\npushi {p.parser.variaveis[p[1]][4]}\npadd\n", p[3] + f"pushi {col}\n" + "mul\n" + p[6] + "add\n" , "storen\n")
        #(i*numeroTotalcolunas) + j

def p_VarArray_var(p):
    "VarArray : var"
    if p[1] not in p.parser.variaveis:
        p[0] = f"err \"ERROR. Variavel nao declarada:\"\n"
        print(f"ERROR. Variavel nao declarada:'{p[1]}'")
        parser.success = False
    else:
        p[0] = (f"storeg {p.parser.variaveis[p[1]][1]}\n",f"pushg {p.parser.variaveis[p[1]][1]}\n")



def p_error(p):
    print('Erro sintático: ', p)
    parser.success = False


# Build the parser
parser = yacc.yacc()
parser.variaveis = {}
parser.sp = 0
parser.labelCount = 0
parser.loopCount = 0
parser.elemsCount = 0
parser.elems2Count = 0
parser.bool = 1


# Read line from input and parser it
import sys

def main():
    choice = '1'

    print("\n\033[1;36m* * * * * MENU * * * * *\033[00m\n")
    print("\033[;1m1 - \033[00mQuery 1")
    print("\033[;1m2 - \033[00mQuery 2")
    print("\033[;1m3 - \033[00mQuery 3")
    print("\033[;1m4 - \033[00mQuery 4")
    print("\033[;1m5 - \033[00mInsert Input File")

    print("\n\033[1;36m* * * * * * * * * * * * *\033[00m\n")
    choice = input ("\033[33m>> \033[00m")

    if choice == "5":
        menu_5()
    elif choice == "4":
        get_files("q4")
    elif choice == "3":
        get_files("q3")
    elif choice == "2":
        get_files("q2")
    elif choice == "1":
        get_files("q1")
    else:
        print("\033[1;31mInvalid Option!\n\033[00m")

def menu_5():
    try:
        #print()
        fInput = input("Insert name of the input file:")
        fread = open("test_files/"+fInput, "r")
        fOutput = input("Insert name of the output file:")
        global fwrite 
        fwrite= open("test_files/"+fOutput,"w+")
        content = fread.read()
        res = parser.parse(content)
        print(parser.variaveis)
        fwrite.close()
    except:
        print('\033[1;31mError. Input file does not exist.\n\033[00m')
    

def get_files(file):
    fread = open("test_files/"+file+"_code.txt", "r")
    global fwrite 
    fwrite = open("test_files/"+file+"_vm.txt","w+")
    content = fread.read()
    res = parser.parse(content)
    print(parser.variaveis)
    fwrite.close()

fwrite = ""
main()