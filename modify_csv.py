import csv

input_file = 'data_Edu.csv'
output_file = 'data_Edu.csv'

# Ouvrez le fichier d'entrée en spécifiant l'encodage
with open(input_file, 'r', encoding='utf-8') as csv_file, open(output_file, 'w', newline='', encoding='utf-8') as output_csv:
    reader = csv.reader(csv_file)
    writer = csv.writer(output_csv)

    for row in reader:
        modified_row = [item.replace('\\', ' ') for item in row]
        writer.writerow(modified_row)

print("La modification du fichier CSV est terminée.")