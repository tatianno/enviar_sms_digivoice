import os
from settings import pasta_mensagens

class DadosCsv():

    def __init__(self):
        #Verificando se o diretorio para monitorar arquivos existe
        if not os.path.isdir(pasta_mensagens):
            os.mkdir(pasta_mensagens)

    def get_arquivos(self):
        caminhos = [os.path.join(pasta_mensagens, nome) for nome in os.listdir(pasta_mensagens)]
        arquivos = [arq for arq in caminhos if os.path.isfile(arq)]
        return [arq for arq in arquivos if arq.lower().endswith(".csv")]