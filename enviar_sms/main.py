#!/usr/local/enviar_sms_digivoice/enviar_sms/venv/bin/python                                                                                                                 
import csv                                                                                                                                                                   
import os                                                                                                                                                                    
import codecs                                                                                                                                                                
from classes.digivoice import Digivoice                                                                                                                                      
from classes.dados_csv import DadosCsv                                                                                                                                       
from settings import grupo_portas_gsm, delimitador                                                                                                                           
                                                                                                                                                                             
#Instanciando objetos                                                                                                                                                        
digivoice = Digivoice(grupo_portas_gsm)                                                                                                                                      
dados_csv = DadosCsv()                                                                                                                                                       
lista_mensagens = []                                                                                                                                                         
#Obtendo lista de arquivos                                                                                                                                                   
arquivos_csv = dados_csv.get_arquivos()                                                                                                                                      
                                                                                                                                                                             
for arquivo in arquivos_csv:                                                                                                                                                 
    lista_mensagens += csv.reader(codecs.open(arquivo, 'rU', 'utf-16'), delimiter=delimitador)                                                                               
    os.remove(arquivo)                                                                                                                                                       
                                                                                                                                                                             
digivoice.enviar_sms(lista_mensagens)