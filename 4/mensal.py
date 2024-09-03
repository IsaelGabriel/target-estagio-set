faturamento: dict = {
    "SP": 67836.43, 
    "RJ": 36678.66, 
    "MG": 29229.88, 
    "ES": 27165.48, 
    "Outros" : 19849.53 
}

total = 0

for item in faturamento.items():
    total += item[1]

for key in faturamento.keys():
    percentage = (100 * faturamento[key]) / total

    print("%s = %.2f%%" % (key, percentage))