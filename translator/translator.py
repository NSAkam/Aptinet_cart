from PySide2.QtCore import QObject, Property, Signal, Slot
from xml.etree import ElementTree
import json

from scripts.config import ConfigManager
from scripts.scanner import Scanner



class QMLLanguageManager(QObject):
    _how: str = ""
    _where: str = ""
    _why: str = ""
    
    language_data_Changed = Signal()

    def __init__(self):
        super().__init__()
        scanner = Scanner(name="scanner1", type="2", model="esg")     
        self.config_manager = ConfigManager(scanner)
           
    def get_how(self):
        return self._how
    
    def set_how(self, value):
        self._how = value
        self.language_data_Changed.emit()
    
    read_how = Property(str, get_how, set_how, notify=language_data_Changed)
        
        
    def get_where(self):
        return self._where
    
    def set_where(self, value):
        self._where = value
        self.language_data_Changed.emit()
    
    read_where = Property(str, get_where, set_where, notify=language_data_Changed)
    
    
    def get_why(self):
        return self._why
    
    def set_why(self, value):
        self._why = value
        self.language_data_Changed.emit()
    
    read_why = Property(str, get_why, set_why, notify=language_data_Changed)    
    
    
    def load_language_data(self, lang):
        try:
            xml_file = f"{lang}.xml"
            tree = ElementTree.parse(xml_file)
            root = tree.getroot()
            for i, line in enumerate(root.findall('line')):
                if i == 0:
                    line1_text = line.text
                    self.set_how(line1_text)
                elif i == 1:
                    line2_text = line.text
                    self.set_why(line2_text)
                elif i == 2:
                    line3_text = line.text
                    self.set_where(line3_text)
        except Exception as e:
            print(f"Error loading texts from XML: {e}")
    
    @Slot(str)
    def change_language(self, language):
        self.load_language_data(language)
        self.config_manager.set_language(language)
        self.config_manager.save()

