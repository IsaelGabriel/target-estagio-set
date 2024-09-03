import json


json_file = open("faturamento.json", "r") # open json file

values_list = json.loads(json_file.read()) # convert json file into list

values_list = [i for i in values_list if i != 0] # remove zeroes from list

values_list.sort()

median = 0.0

for value in values_list:
    median += float(value) # converts to float in case there are integers in the list

median /= len(values_list)

above_average_days = 0

while(values_list[-(above_average_days + 1)] > median):
    above_average_days += 1


print("Menor faturamento: ", values_list[0])
print("Maior faturamento: ", values_list[-1])
print("Dias acima da média: ", above_average_days)