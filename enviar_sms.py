import csv
from classes.digivoice import Digivoice
from classes.dados_csv import DadosCsv
from settings import grupo_portas_gsm

#Variaveis
lista_mensagens = []
#Instanciando objetos
digivoice = Digivoice(grupo_portas_gsm)
dados_csv = DadosCsv()
#Obtendo lista de arquivos
arquivos_csv = dados_csv.get_arquivos()

for arquivo in arquivos_csv:
    with open(arquivo, 'rt') as ficheiro:
        lista_mensagens += csv.reader(ficheiro)
            
#print(lista_mensagens)
digivoice.enviar_sms(lista_mensagens)

        

            