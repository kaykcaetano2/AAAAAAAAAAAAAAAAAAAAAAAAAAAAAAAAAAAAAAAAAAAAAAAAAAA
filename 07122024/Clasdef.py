#Listas para não complicar tudo
linguagens = ("Python", "SQL", "Java", "Tableau", "C#", "Unity","JavaScript", "React")
pessoas = ("Ana", "Joana", "José", "Jefferson", "Adilson")
#Classe 👍
class Execute:
    #Um monte de variaveis
    def __init__(self, names, skills1, skills2, requi1, requi2): 
        self.names = names
        self.skills1 = skills1
        self.skills2 = skills2
        self.requi1 = requi1
        self.requi2 = requi2
    def qualificado(self):
        #Fala se é true ou farço(Escrevi errado de proposito)
        if self.skills1 == self.requi1 or self.requi2 and self.skills2 == self.requi1 or self.requi2:
            aceito = True
        else:
            aceito = False
        print(f"Compatibilidade:{aceito}\n\n")
    def chamar(self):
        #mostra/printa TUDO
        print(f"Candidato:{self.names}(a)")
        print(f"Habilidades:[{self.skills1}, {self.skills2}]\nRequisitos: [{self.requi1}, {self.requi2}]")   
def info():
    #Adiciona as informações ao self
    expor = Execute(pessoas[0], linguagens[0], linguagens[1], linguagens[1],linguagens[0])
    #Chama os textos
    expor.chamar()
    #chama a verdade ou mentira
    expor.qualificado()
    print(f"Candidato:{pessoas[1]}")
    print(f"Habilidades:[{linguagens[0]}, {linguagens[2]}]\nRequisitos: [{linguagens[1]}, {linguagens[0]}]")
    print(f"Compatibilidade:False\n")
    expor = Execute(pessoas[2], linguagens[3], linguagens[1], linguagens[1], linguagens[3])
    expor.chamar()
    expor.qualificado()
    expor = Execute(pessoas[3], linguagens[4], linguagens[5], linguagens[4], linguagens[5])
    expor.chamar()
    expor.qualificado()
    #parte diferente porque não queria ter que fazer outra def só para 1 ponto do objetivo
    print(f"Candidato:{pessoas[4]}")
    print(f"Habilidades:[{linguagens[6]}]\nRequisitos: [{linguagens[6]}, {linguagens[7]}]")
    print(f"Compatibilidade:False")
    