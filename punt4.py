

from xml.dom import minidom
doc = minidom.parse("punt1.xml")

tag_mostrar = doc.documentElement

file = open("RRHH.html", "w")
file.write("<html><head><title>Informació del personal</title></head><body>\n")
llista_tag_persona = tag_mostrar.getElementsByTagName("person")

for persona in llista_tag_persona:
    valor_id = persona.getAttribute("id")
    valor_name = persona.getElementsByTagName("name")[0].firstChild.data
    valor_age = persona.getElementsByTagName("age")[0].firstChild.data
    valor_cumple = persona.getElementsByTagName("naixement")[0].firstChild.data
    gender = persona.getElementsByTagName("name")[0].getAttribute("gender")

    file.write("<p>")
    file.write(f"<strong>ID:</strong> {valor_id}<br>")
    file.write(f"<strong>Name:</strong> {valor_name}<br>")
    file.write(f"<strong>Gender:</strong> {gender}<br>")
    file.write(f"<strong>Age:</strong> {valor_age}<br>")
    file.write(f"<strong>Birthdate:</strong> {valor_cumple}<br>")
    file.write("</p>\n")

file.write("</body></html>")
file.close()