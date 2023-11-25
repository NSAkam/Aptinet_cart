from Services.dal import DAL
from Repositories.factoreRepository import UserFactoreRepository


class UserFactoreModel:
    repository : UserFactoreRepository
    
    def __init__(self, dataAccessLayer: DAL) -> None:
        self.repository = UserFactoreRepository(dataAccessLayer)
        
    def get_factoreByPhone(self, phone: str) -> int:
        return self.repository.get_factoreByPhone(phone)
    
    def get_factoreByEmail(self, email: str):
        return self.repository.get_factoreByEmail(email)
    
    def get_factoreById(self, id):
        return self.repository.get_factoreById(id)
        
        
        
    
    