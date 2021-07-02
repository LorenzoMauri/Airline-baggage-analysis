
from pymongo import MongoClient
import json

class Mongodb: 
    def __init__(self) -> None:
        self._user =  None
        self.port =  None
        self._password =  None
        self.host = None
        self._config = None
    
    def open_connection(self):
        """Opens Mongodb connection through an external configuration

        Returns:
             mongoclient object  : client mongodb
        """       
        client = MongoClient('localhost', self.port, username=self._user, password=self._password)
        return client 

    def set_configuration(self, config_pathname, database) : 
        """
        Sets configurations (i.e username or hostname to open mongodb connection)

        :param config_pathname: configuration file pathname
        :type config_pathname: str 
        :param database: database to configure 
        :type database: str 
        """        
        with open(config_pathname, 'r') as config :
            config_file =  json.load(config)
            connection_config = config_file.get(database).get('connection') 
            self._user = connection_config.get('user') 
            self.port = connection_config.get('port') 
            self._password = connection_config.get('password') 
            self.host = connection_config.get('host') 