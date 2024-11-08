# Escritura en archivo binario
datos = b"Estos son algunos datos binarios."
with open("archivo_binario.bin", "wb") as file:
    file.write(datos)

# Lectura de archivo binario
with open("archivo_binario.bin", "rb") as file:
    contenido = file.read()
    print("Datos leídos en formato binario:", contenido)
