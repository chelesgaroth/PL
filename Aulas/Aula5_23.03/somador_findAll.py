# Aula 5: 2021-03-23
# 
# Somador On/Off
#
# Quando recebe um ON o semáforo liga-se e faz a soma dos valores dados => soma = soma + valor('\d+')
# Quando recebe um OFF desliga-se
# Quando recebe um '=' então ele mostra o resultado da soma
#

import sys
import re

# My state - Inicializar o semaforo
semaforo = True
soma = 0

# Reading input  
for linha in sys.stdin:
    if ( res := re.findall(r'([oO][nN])|([oO][fF]{2})|(\d+)|(=)',linha)):
        for (on,off,dig,pr) in res:
            if on:
                semaforo = True
            elif off:
                semaforo = False
            elif dig:
                if semaforo:
                    soma = soma + int(dig)
            else:
                print(soma)
    else:
        pass

'''
Juntamos as expressões regulares todas numa, mas caso tivessemos mais expressões seria pouquíssimo eficiente. 
Caso tivéssemos mais casos seria super complicado.
Portanto a solução é usar uma ferramenta criada para isso: FLEX 

'''
