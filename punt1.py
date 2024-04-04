

from xml.dom import minidom

doc = minidom.parse("punt1.xml")

tag_principal = doc.documentElement

#Element principal del document
nom_tag_principal=tag_principal.nodeName

