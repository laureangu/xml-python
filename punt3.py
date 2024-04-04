

from xml.dom import minidom
from datetime import datetime
dataActual = datetime.now()
doc = minidom.parse("punt1.xml")

tag_mostrar = doc.documentElement
tag_people = tag_mostrar.getElementsByTagName("people")[0]
llista_tag_persona = tag_people.getElementsByTagName("person")

for tag_people in llista_tag_persona:
    tag_name = tag_people.getElementsByTagName("name")[0]
    valor_name = tag_name.firstChild.data
    valor_age = tag_people.getElementsByTagName("age")[0].firstChild.data
    valor_cumple = tag_people.getElementsByTagName("naixement")[0].firstChild.data
    gender = tag_name.getAttribute("gender")
    id = tag_people.getAttribute("id")  
    any = int(valor_cumple[:4])
    if valor_cumple[5:7] == "01":
        mes = "gener"
    elif valor_cumple[5:7] == "02":
        mes = "febrer"
    elif valor_cumple[5:7] == "03":
        mes = "març"
    elif valor_cumple[5:7] == "04":
        mes = "abril"
    elif valor_cumple[5:7] == "05":
        mes = "maig" 
    elif valor_cumple[5:7] == "06":
        mes = "juny"
    elif valor_cumple[5:7] == "07":
        mes = "juliol"
    elif valor_cumple[5:7] == "08":
        mes = "agost"
    elif valor_cumple[5:7] == "09":
        mes = "setembre"
    elif valor_cumple[5:7] == "10":
        mes = "octubre"
    elif valor_cumple[5:7] == "11":
        mes = "novembre"
    elif valor_cumple[5:7] == "12":
        mes = "desembre"
    meset = int(valor_cumple[5:7])
    dia = int(valor_cumple[8:10])    

    any_actual = dataActual.year
    edad_actual = any_actual - any
    mes_actual = dataActual.month
    dia_actual = dataActual.day
    if (mes_actual, dia_actual) < (any, dia):
        edad_actual -= 1
        
    if edad_actual == any:
        fals = ("Tot correcte")
    else: 
        fals = (f"Esta enganyant al Curriculum. Diu al CV que la seva edat es {valor_age}.")

    print(f"La persona {valor_name} amb DNI {id} y es sent amb identitat {gender}. Te {edad_actual} anys i va neixer el {dia} de {mes} del {any}. {fals}")

print("Mostra del programa.")