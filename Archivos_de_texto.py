
with open("archivo_texto.txt", "w") as file:
    file.write("Primera línea del archivo de texto.\n")
    file.write("Segunda línea del archivo de texto.\n")

with open("archivo_texto.txt", "r") as file:
    contenido = file.read()
    print("Contenido completo del archivo:\n", contenido)

with open("archivo_texto.txt", "r") as file:
    for linea in file:
        print("Línea:", linea.strip())

with open("archivo_texto.txt", "a") as file:
    file.write("Línea añadida al final del archivo.\n")
