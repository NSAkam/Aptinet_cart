from xml.dom import minidom
from xml.etree import ElementTree as ET
import json


from PySide2.QtCore import QObject, Signal, Property, Slot, QThread


class languageReader(QObject):
    

    def __init__(self,namefile):
        f = open("../../" +namefile+".json", "r")
        s= f.read()
        self.lst = json.loads(s)
        super().__init__()



    def get_txt_welcome(self):
        return print(self.lst["welcome!"])
    
    txt_welcome = Property(str,get_txt_welcome)

    def get_txt_Toaquickshoppingexperience(self):
        return print(self.lst["To a quick shopping experience"])
    
    txt_Toaquickshoppingexperience =Property (str,get_txt_Toaquickshoppingexperience)