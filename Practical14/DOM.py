import xml.dom.minidom
import os
from datetime import datetime
start_time=datetime.now()
os.chdir(r"F:\^Course Material\IBI1\IBI1_2024-25\Practical14")


DOMTree=xml.dom.minidom.parse("go_obo.xml")
terms=DOMTree.documentElement.getElementsByTagName("term")
count1=[]
count2=[]
count3=[]
def max_locate(count,ns):
    number=[]

    maximum=max(count)
    for term in terms:
        if (term.getElementsByTagName('namespace')[0].firstChild.nodeValue == ns and len(term.getElementsByTagName("is_a")) == maximum):
            number.append(term.getElementsByTagName('id')[0].firstChild.nodeValue)           
    print("The term that has the most is_a is",number, "with", maximum, "is_a.")


for term in (terms):
    if term.getElementsByTagName('namespace')[0].firstChild.nodeValue=="biological_process":
        count1.append(len(term.getElementsByTagName("is_a")))
                 
    elif term.getElementsByTagName('namespace')[0].firstChild.nodeValue=="molecular_function":
        count2.append(len(term.getElementsByTagName("is_a")))

    elif term.getElementsByTagName('namespace')[0].firstChild.nodeValue=="cellular_component":
        count3.append(len(term.getElementsByTagName("is_a")))

max_locate(count1, "biological_process")
max_locate(count2, "molecular_function")
max_locate(count3, "cellular_component")

finish_time=datetime.now()
print("runtime:", finish_time-start_time)

#SAX is much faster than DOM