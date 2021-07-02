
# -*- coding: utf-8 -*-

"""
Created on Sat Mar  7 10:01:15 2020

@author: loren
"""

import mysql.connector
import datetime
import decimal
import json 
   
class Processing_dati:
    def __init__(self,mongoPort):
        self.mongoPort=mongoPort
        
    def importa_dati(self,nome_tabella):
        self.nome_tabella=nome_tabella
        query = f"describe {self.nome_tabella} ;"
        nome_colonne=Processing_dati(self.mongoPort).estrazione_dati(query)
        nome_colonne=[nome_colonne[i][0] for i in range(0,len(nome_colonne))]
        dati=Processing_dati(self.mongoPort).estrazione_dati(f"select * from {self.nome_tabella}")
        dati_collezione_mongo=[]
        for row in dati : 
            dic={}
            lista=list(row)
            for i in range(0,len(nome_colonne)):
                if isinstance(lista[i], datetime.date)==True :        
                    dic[nome_colonne[i]]=lista[i].strftime('%Y-%m-%d %H:%M:%S')    
                elif isinstance(lista[i], decimal.Decimal) == True : 
                    dic[nome_colonne[i]] = float(lista[i])   
                else : 
                    dic[nome_colonne[i]]=lista[i]
            dati_collezione_mongo.append(dic)
        Processing_dati(self.mongoPort).connessione_mongo().dati_datamanagement[self.nome_tabella].insert_many(dati_collezione_mongo)
        
    def esporta_dati(self,nome_tabella):
        self.nome_tabella=nome_tabella
        #export_path = '/home/studente/EXPORTED-data/'+nome_tabella+'.csv'
        collection=Processing_dati(self.mongoPort).connessione_mongo().dati_datamanagement[self.nome_tabella]
        cursor=collection.find({},{'_id': False})
        s='['
        with open('/home/studente/EXPORTED-data/'+self.nome_tabella+'.json','w+') as output :    
            for document in cursor :            
                stringa=json.dumps(document)+','
                s+=stringa    
            s+=']'
            output.write(s[:-2]+s[-1])
        output.close()
        #df = pd.DataFrame(list_of_documents)
        #df.to_csv(export_path,header=True,index=False)
        print( 'mongodb collection exported successfully !')
        
    
if __name__ == '__main__':
    d=Processing_dati(27011)
        
