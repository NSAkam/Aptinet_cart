import json
from scripts.scanner import Scanner
from PySide2.QtCore import QObject, Property, Signal, Slot



class ConfigManager(QObject):
    @Signal
    def changed(self):
        pass
       
    def __init__(self, scanner, language="") -> None:
        super().__init__()
        self.scanner = scanner
        self._language = language
        
    def get_language(self):
        return self._language
        # print(self._language)
    
    def set_language(self, value):
        self._language = value
        self.changed.emit()
        # print(self._language)
        
    read_language = Property(str, get_language, set_language, notify=changed)
    

    def save(self):
        data = {
            "scanner": {
                "name": self.scanner.get_name(),
                "type": self.scanner.get_type(),
                "model": self.scanner.get_model()
            },
            "language": self.get_language()
        }
        with open("config.json", "w") as json_file:
            json.dump(data, json_file, indent = 2)
            print("Data stored in json file successfully .")
            
    def load(self):
        with open("config.json") as json_file:
            data = json.load(json_file)
            scanner_data = data.get("scanner")
            self.scanner.set_name(scanner_data.get("name"))
            self.scanner.set_type( scanner_data.get("type"))
            self.scanner.set_model(scanner_data.get("model"))
            self.set_language(data.get("language"))
    
            
# if __name__ == "__main__":
#     scanner = Scanner(name="scanner1", type="2", model="esg")     
#     config = ConfigManager(scanner, "en")
#     config.save()
    # config.load()
    # print(config.read_language)
    

        
        