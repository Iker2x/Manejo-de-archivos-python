import csv

# Escritura de archivo CSV
with open("archivo.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["ID", "Nombre"])
    writer.writerow([1, "Juan"])
    writer.writerow([2, "Ana"])

# Lectura de archivo CSV
with open("archivo.csv", "r") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(row)
