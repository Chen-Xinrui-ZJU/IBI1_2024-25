import xml.sax
import os
from datetime import datetime
start_time=datetime.now()
os.chdir(r"F:\^Course Material\IBI1\IBI1_2024-25\Practical14")

class is_aHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.current_tag = ""
        self.isa=0
        self.id=""
        self.in_term=False
        self.namespace=""
        self.count1=[]
        self.count2=[]
        self.count3=[]
        self.id1=[]
        self.id2=[]
        self.id3=[]
    
    def startElement(self, tag, attrs):
        self.current_tag=tag
        if tag == "term":
            self.in_term=True
            self.id=""
            self.namespace=""
            self.isa=0
        elif self.in_term and tag == "is_a":
            self.isa += 1 
    def characters(self, content):
        if self.in_term:  
            if self.current_tag == "namespace":              
                self.namespace += content.strip()
            elif self.current_tag == "id":
                self.id += content.strip()
            
    def endElement(self, tag):
        if tag == "term":
            if self.namespace == "biological_process":
                self.count1.append(self.isa)
                self.id1.append(self.id)
            if self.namespace == "molecular_function":
                self.count2.append(self.isa)
                self.id2.append(self.id)
            if self.namespace == "cellular_component":
                self.count3.append(self.isa)
                self.id3.append(self.id)
            self.isa=0
            self.id=""
            self.in_term=False
            self.namespace=""
            self.current_tag=""

parser=xml.sax.make_parser()
handler=is_aHandler()
parser.setContentHandler(handler)
parser.setFeature(xml.sax.handler.feature_namespaces,0)
parser.parse("go_obo.xml")

if handler.count1:
    max_count = max(handler.count1)
    max_indices = [i for i, v in enumerate(handler.count1) if v == max_count]
    print("biological_process:")
    for idx in max_indices:
        print("  ", handler.id1[idx], "with", handler.count1[idx], "<is_a>")

if handler.count2:
    max_count = max(handler.count2)
    max_indices = [i for i, v in enumerate(handler.count2) if v == max_count]
    print("molecular_function:")
    for idx in max_indices:
        print("  ", handler.id2[idx], "with", handler.count2[idx], "<is_a>")

if handler.count3:
    max_count = max(handler.count3)
    max_indices = [i for i, v in enumerate(handler.count3) if v == max_count]
    print("cellular_component:")
    for idx in max_indices:
        print("  ", handler.id3[idx], "with", handler.count3[idx], "<is_a>")

finish_time=datetime.now()
print("runtime:", finish_time-start_time)

#SAX is much faster than DOM