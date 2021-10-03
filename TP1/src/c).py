import re
from collections import Counter

f = open("processos.xml", "r")
content = f.read()
contador = 0
listaP = []


observacoes = re.findall(r'(<obs>(\n|.)*?</obs>)', content)
for obs in observacoes:
    res2 = re.findall(r'(Irmao|Tio|Primo)', obs[0])

    if (res2):
        contador+=1
        for x in res2:
            listaP.append(x)

parFreq = (Counter(listaP).most_common(1))

print("\n\033[36m\033[1mGrau de Parentesco mais frequente:\033[0m ")
for key, value in parFreq:
    print("\033[93m->\033[0m",key)

print("\n\033[36m\033[1mNumero de candidatos que tem parentes eclesiasticos:\033[0m ")
print("\033[93m->\033[0m", contador)