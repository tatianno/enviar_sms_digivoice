#!/usr/local/enviar_sms_digivoice/enviar_sms/venv/bin/python                                                                                                                 
import csv                                                                                                                                                                   
import os                                                                                                                                                                    
import codecs                                                                                                                                                                
from datetime import datetime
from classes.dados_csv import DadosCsv
from classes.db import MysqlConn                                                                                                                                      
from settings import delimitador, db                                                                                                                          

def copiar_dados(): 
    #Instanciando objetos                                                                                                                                                        
    dados_csv = DadosCsv()
    mysql_conn = MysqlConn(db)                                                                                                                                                      
    #Obtendo lista de arquivos                                                                                                                                                   
    arquivos_csv = dados_csv.get_arquivos()
    registros = 0
    erros = 0                                                                                                                                     
                                                                                                                                                                                
    for arquivo in arquivos_csv:   
        
        try:                                                                                                                                             
            dados = list(
                csv.reader(
                    codecs.open(
                        arquivo, 
                        'rU', 
                        'utf-16'
                    ), 
                    delimiter=delimitador
                )
            )[0]
            query = """INSERT INTO mensagens (
                destino,
                mensagem,
                arquivo
            ) VALUES (
                '{}',
                '{}',
                '{}',
                '{}'
            )     
            """.format(
                dados[0],
                dados[3],
                arquivo
            )
            mysql_conn.query(query)
            registros += 1
            
        except:
            erros += 1

        os.remove(arquivo)                                                                                                                                                       

    mysql_conn.disconnect()
    return {
        'salvos' : registros,
        'erros' : erros
    }                                                                                                                                                      