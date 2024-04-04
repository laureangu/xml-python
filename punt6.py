

from xml.dom import minidom

# Parsear el XML
doc = minidom.parse("punt1.xml")
tag_mostrar = doc.documentElement

# Crear el documento HTML
html_doc = minidom.Document()
html = html_doc.createElement('html')
html_doc.appendChild(html)

head = html_doc.createElement('head')
html.appendChild(head)

title = html_doc.createElement('title')
title_text = html_doc.createTextNode('Informació del personal')
title.appendChild(title_text)
head.appendChild(title)

body = html_doc.createElement('body')
html.appendChild(body)

# Iterar sobre cada elemento person
llista_tag_persona = tag_mostrar.getElementsByTagName("person")

for persona in llista_tag_persona:
    valor_id = persona.getAttribute("id")
    valor_name = persona.getElementsByTagName("name")[0].firstChild.data
    valor_age = persona.getElementsByTagName("age")[0].firstChild.data
    valor_cumple = persona.getElementsByTagName("neixement")[0].firstChild.data
    gender = persona.getElementsByTagName("name")[0].getAttribute("gender")

    h2 = html_doc.createElement('h2')
    h2_text = html_doc.createTextNode(f'{valor_id} - {valor_name}')
    h2.appendChild(h2_text)
    body.appendChild(h2)

    ul = html_doc.createElement('ul')

    li_age = html_doc.createElement('li')
    li_age_text = html_doc.createTextNode(f'age - {valor_age}')
    li_age.appendChild(li_age_text)
    ul.appendChild(li_age)

    li_gender = html_doc.createElement('li')
    li_gender_text = html_doc.createTextNode(f'sexe - {gender}')
    li_gender.appendChild(li_gender_text)
    ul.appendChild(li_gender)

    li_naixement = html_doc.createElement('li')
    li_naixement_text = html_doc.createTextNode(f'neixement - {valor_cumple}')
    li_naixement.appendChild(li_naixement_text)
    ul.appendChild(li_naixement)

    body.appendChild(ul)

# Guardar el document HTML en un arxiu, asegurant que es tanqui al finalitzar.
with open("RRHH.html", "w") as file:
    file.write(html_doc.toprettyxml())