import xml.etree.ElementTree as ET

# Crear archivo XML
root = ET.Element("biblioteca")
libro = ET.SubElement(root, "libro")
titulo = ET.SubElement(libro, "titulo")
titulo.text = "Aprendiendo Python"
autor = ET.SubElement(libro, "autor")
autor.text = "Juan Pérez"

# Guardar en archivo
tree = ET.ElementTree(root)
tree.write("archivo.xml")

# Leer el archivo XML
tree = ET.parse("archivo.xml")
root = tree.getroot()
for libro in root:
    for detalle in libro:
        print(f"{detalle.tag}: {detalle.text}")
