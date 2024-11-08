import json

# Escritura de archivo JSON
datos = {"ID": 1, "Nombre": "Juan"}
with open("archivo.json", "w") as jsonfile:
    json.dump(datos, jsonfile)

# Lectura de archivo JSON
with open("archivo.json", "r") as jsonfile:
    datos = json.load(jsonfile)
    print("Datos del archivo JSON:", datos)
