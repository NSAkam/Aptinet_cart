from Services.dal import DAL
from Repositories.userRepository import UserRepository

class UserModel():
    repository: UserRepository

    def __init__(self,dataAccessLayer:DAL) -> None:
        self.repository=UserRepository(dataAccessLayer)

    def createUser(self,email:str,regtime:str)->int:
        return self.repository.create_user(email,regtime)