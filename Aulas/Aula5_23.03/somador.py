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

# Reading input  => Neste caso apenas tem em consideração uma opção linha a linha ou seja se tivermos 3 números na mesma linha não soma os 3
for linha in sys.stdin:
    if (re.search(r'[oO][nN]',linha)):
        semaforo = True
    elif (re.search(r'[oO][fF]{2}', linha)):
        semaforo = False
    elif m := re.search(r'(\d+)',linha):
        if(semaforo==True):
            soma = soma + int(m.group(1))
    elif (re.search(r'=', linha)):
        print(soma)
    else:
        pass


