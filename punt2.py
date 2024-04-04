

from xml.dom import minidom

doc = minidom.parse("punt1.xml")

#Element principal del document.
tag_mostrar = doc.documentElement
#Fem variables de tags principas.
tag_persona = tag_mostrar.getElementsByTagName("people")[0]
#Recollim la dada que utilitzarem
llista_tag_persona = tag_persona.getElementsByTagName("person")

#Recorrem la llista per a troba els "tags" que utilitzarem. 
#Com be indiquem, només volem el tag d'obertura, obviant el de tancament.
persona=dict()
for tag_persona in llista_tag_persona:
    tag_name = tag_persona.getElementsByTagName("name")[0]
    valor_name = tag_name.firstChild.data
    persona ["nom"] = valor_name
    
    valor_age = tag_persona.getElementsByTagName("age")[0].firstChild.data
    persona ["edat"] = valor_age

    valor_cumple = tag_persona.getElementsByTagName("naixement")[0].firstChild.data
    persona ["cumple"] = valor_cumple

    gent = {
    "persona" : persona
    }
    
    print(f"La persona {persona['nom']}, te {persona['edat']} i va neixer a la següent data {persona['cumple']}")