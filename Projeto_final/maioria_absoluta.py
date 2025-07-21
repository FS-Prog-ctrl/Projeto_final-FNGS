matriz = []
ncandidatos = int(input("Quantos candidatos queres escrever? "))  
Nome_Candidato = []
linha = []
# Percorrendo as linhas i
for i in range(ncandidatos):
    # linha = []
    # Percorrendo as colunas j
    for j in range(2):
        if j==0:
            valor = input(f"Qual o nome do {i+1}ª candidato: ")
            Nome_Candidato.append(valor)
        elif j==1:
            valor = int(input(f"Qual o número de votos do(a) candidato(a) {Nome_Candidato[i]}: "))
        linha.append(valor)
    matriz.append(linha)

for i in range(1):
    linha = []
    # Percorrendo as colunas j
    for j in range(2):
        if j==0:
            valor = "Em Branco"
            Nome_Candidato.append(valor)
        elif j==1:
            valor = int(input(f"Qual o número de votos 'Em Branco': "))
        linha.append(valor)
    matriz.append(linha)

for i in range(1):
    linha = []
    # Percorrendo as colunas j
    for j in range(2):
        if j==0:
            valor = "Nulos"
            Nome_Candidato.append(valor)
        elif j==1:
            valor = int(input(f"Qual o número de votos 'Nulos': "))
        linha.append(valor)
    matriz.append(linha)


# Gravar a matriz num ficheiro
with open("votos.csv", "w", encoding="utf-8") as ficheiro:
    for linha in matriz:
        ficheiro.write(f"{linha[0]},{linha[1]}\n")
        # ficheiro.write(f"{linha}\n")