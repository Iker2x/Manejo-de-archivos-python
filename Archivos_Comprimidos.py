import zipfile

# Crear archivo ZIP y agregar archivos
with zipfile.ZipFile("archivo.zip", "w") as zipf:
    zipf.write("archivo_texto.txt")
    zipf.write("archivo_excel.xlsx")

# Extraer contenido de un archivo ZIP
with zipfile.ZipFile("archivo.zip", "r") as zipf:
    zipf.extractall("contenido_extraido")
    print("Archivos extraídos:", zipf.namelist())
