from Mongodb.connection import MongodbConnection
import json
from mysql.connector import connect

class Mysql(MongodbConnection): 
    def __init__(self) -> None:
        self._user =  None
        self.port =  None
        self._password =  None
        self.host = None
        self._config = None
        self.client = None
    
    def open_connection(self, table_name):
        """Opens Mongodb connection through an external configuration

        Returns:
             mongoclient object  : client mongodb
        """       
        self.client = connect(user=self._user, password= self._password,
                         host=self.host, database= table_name)

    def query(self, mysql_query):
        """
        Launches a given MySQL query 
        """        
        interrogazione = self.client.cursor(buffered=True)
        interrogazione.execute(mysql_query) 
        return list(interrogazione)

        

    