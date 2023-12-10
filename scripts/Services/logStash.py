from Services.dal import DAL
from PySide2.QtSql import QSqlQuery
import datetime


class LogStash():

    dal: DAL

    def __init__(self, dataAccessLayer: DAL) -> None:
        self.dal = dataAccessLayer
        self.dal.Connect()

    def insertLog(self, action: str, value: str, user_id: str):
        TotalSeconds = datetime.datetime.now().timestamp()
        query = QSqlQuery()
        if (query.exec_("insert into loggs (action,value,user_id) values ('"+str(action)+"','"+str(value)+"','"+str(user_id)+"')")):
            return True
        else:
            return False
