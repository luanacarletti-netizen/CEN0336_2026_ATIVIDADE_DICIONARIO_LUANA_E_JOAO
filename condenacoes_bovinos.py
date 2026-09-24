# Registro de causas de condenação encontradas
# durante a inspeção post mortem de bovinos.

# No dicionário:
# chave = causa da condenação
# valor = quantidade de ocorrências

condenacoes = { "Cisticercose": 6, "Fasciolose": 8, "Abscesso hepático": 5}

# ACESSO
# Consulta a quantidade de casos de cisticercose.
print("Casos de cisticercose:", condenacoes["Cisticercose"])

# INSERÇÃO
# Adiciona uma nova causa de condenação.
condenacoes["Pneumonia"] = 4

# ATUALIZAÇÃO
# Foram encontrados mais 2 casos de fasciolose.
condenacoes["Fasciolose"] = condenacoes["Fasciolose"] + 2

# GET()
# Consulta uma causa que não está registrada.
# Se não existir, retorna 0.
casos_tuberculose = condenacoes.get("Tuberculose", 0)

print("Casos de tuberculose:", casos_tuberculose)

# ITEMS()
# Mostra todas as causas e suas quantidades.
print("\nCausas de condenação registradas:")

for causa, quantidade in condenacoes.items():
    print(causa, ":", quantidade)


Ao rodar o scrip no python3 condenacoes_bovinos.py o resultado encontrado é:

Casos de cisticercose: 6
Casos de tuberculose: 0

Causas de condenação registradas:
Cisticercose : 6
Fasciolose : 10
Abscesso hepático : 5
Pneumonia : 4