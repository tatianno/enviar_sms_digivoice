#!/usr/local/enviar_sms_digivoice/enviar_sms/venv/bin/python
from time import sleep       
from datetime import datetime                                                                                                                                                                                                                                                                        
from classes.digivoice import Digivoice                                                                                                                                      
from classes.db import MysqlConn
from funcoes import copiar_dados
from settings import grupo_portas_gsm, db                                                                                                                         
                                                                                                                                                                             
#Instanciando objetos 
digivoice = Digivoice(grupo_portas_gsm)                                                                                                                                      

while True:
    copiar_dados()
    mysql_conn = MysqlConn(db)
    lista_mensagens = []                                                                                                                                     
    fields = 'id, destino, mensagem, enviado'
    query = "SELECT {} FROM mensagens WHERE enviado = 0".format(
        fields 
    )

    for (
        id,
        destino, 
        mensagem, 
        enviado
    ) in mysql_conn.query(query):                                                                                                                                                
        lista_mensagens.append(
            {
                'id' : id,
                'destino' : destino,
                'mensagem' : mensagem
            }
        )
                                                                                                                                                    
    ids_enviados = digivoice.enviar_sms(lista_mensagens)

    for id in ids_enviados:
        query = "UPDATE mensagens SET enviado = 1, data_envio = {} WHERE id = {}".format(
            id,
            datetime.today().strftime('%Y-%m-%d %H:%M:%S')
        )
        resultado = mysql_conn.query(query)

    mysql_conn.disconnect()
    sleep(300)