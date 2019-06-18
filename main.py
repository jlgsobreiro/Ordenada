class No:

    def __init__(self, nome):
        self.nome = nome
        self.rotas = {"custo": [], "direcao": []}

    def cheaper(self, list):
        cheap = {"custo": 99, "direcao": None}
        i = 0
        while i < len(self.rotas["direcao"]):
            if cheap["custo"] > self.rotas["custo"][i] and self.rotas["direcao"][i] not in list:
                cheap["custo"] = self.rotas["custo"][i]
                cheap["direcao"] = self.rotas["direcao"][i]
            i += 1
        return cheap

    def cheap_from_list(self, list):
        cheap = {"custo": 99, "direcao": None}
        for x in list:
            if cheap["custo"] > x["custo"]:
                cheap = x
        return cheap


A = No("A")
B = No("B")
C = No("C")
D = No("D")
E = No("E")
F = No("F")
G = No("G")

A.rotas = {"custo": [9, 13, 5], "direcao": [B, D, C]}
B.rotas = {"custo": [9, 10, 3], "direcao": [A, E, D]}
C.rotas = {"custo": [5, 12], "direcao": [A, F]}
D.rotas = {"custo": [13, 3, 6, 14], "direcao": [A, B, E, G]}
E.rotas = {"custo": [10, 6, 7], "direcao": [B, D, G]}
F.rotas = {"custo": [12, 10], "direcao": [C, G]}
G.rotas = {"custo": [7, 14, 10], "direcao": [E, D, F]}

lista_fechados = []
lista_abertos = []
no_candidato = A
sucesso = False
i = 0
j = 0
while i < len(A.rotas["direcao"]):
    lista_abertos.insert(i, {"custo": A.rotas["custo"][i], "direcao": A.rotas["direcao"][i], "origem": A})
    i += 1

while not sucesso or len(lista_abertos) > 0:
    i = 0
    menor_custo = 99
    while i < len(lista_abertos):
        if menor_custo > lista_abertos[i]["custo"]:
            menor_custo = lista_abertos[i]["custo"]
            no_candidato = lista_abertos[i]
        i += 1

    lista_fechados.insert(j, lista_abertos.pop(lista_abertos.index(no_candidato)))
    j += 1
    if no_candidato["direcao"] == G:
        sucesso = True
    else:
        i = 0
        while i < len(no_candidato["direcao"].rotas["direcao"]):
            obj = {"custo": no_candidato["direcao"].rotas["custo"][i],
                   "direcao": no_candidato["direcao"].rotas["direcao"][i],
                   "origem": no_candidato["direcao"]}
            if obj not in lista_abertos and obj not in lista_fechados:
                lista_abertos.insert(i, obj)
            i += 1

for x in lista_fechados:
    print(x["origem"].nome + "->" + x["direcao"].nome + ": " + str(x["custo"]))

print("\n\n")
# teste = lista_fechados.pop(0)
teste1 = A
custo_total = 0
while len(lista_fechados) > 0:
    i = 0
    for x in lista_fechados:
        if teste1 == x["origem"]:
            if x["direcao"] not in lista_abertos:
                lista_abertos.insert(len(lista_abertos), teste1)
                teste1 = x["direcao"]
                custo_total += lista_fechados[i]["custo"]
                buf = lista_fechados.pop(i)

                print(buf["origem"].nome + "->" + buf["direcao"].nome + ": " + str(buf["custo"]))
        if teste1.nome == G.nome:
            teste1 = A
            print(str(custo_total))
            custo_total = 0
            while lista_abertos:
                lista_abertos.pop(0)
        i += 1
