import csv
import os
from time import sleep
from classes.digivoice import Digivoice
from classes.dados_csv import DadosCsv
from settings import grupo_portas_gsm

#Instanciando objetos
digivoice = Digivoice(grupo_portas_gsm)
dados_csv = DadosCsv()

while True:
    lista_mensagens = []
    #Obtendo lista de arquivos
    arquivos_csv = dados_csv.get_arquivos()

    for arquivo in arquivos_csv:
        with open(arquivo, 'rt') as ficheiro:
            lista_mensagens += csv.reader(ficheiro)
        
        os.remove(arquivo)
                
    digivoice.enviar_sms(lista_mensagens)

        

            