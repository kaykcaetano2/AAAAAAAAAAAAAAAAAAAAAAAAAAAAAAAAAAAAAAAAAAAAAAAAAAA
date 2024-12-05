#importar
from Clasdef import info
#Perguntar para a inicialização
inicio = str(input("Gostaria de observar as vagas que estão sendo disputadas?(sim/não)\n"))
if inicio == "sim":
    info()
else:
    print("Ok, pergunto outra hora")
#Resto no outro arquivo