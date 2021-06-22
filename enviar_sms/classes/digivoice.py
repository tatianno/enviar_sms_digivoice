import logging
from datetime import datetime
from time import sleep
from unicodedata import normalize
from asterisk.manager import Manager
from settings import ami_login, DEBUG, log_file

logging.basicConfig(
    level=logging.DEBUG, 
    filename=log_file,
    format='%(asctime)s :: %(levelname)s :: %(message)s'
)

class Digivoice():

    def __init__(self, grupo_portas_gsm='g1', intervalo=10):
        self.grupo_portas_gsm = grupo_portas_gsm
        self.manager = Manager()
        self.manager_connect = False
        self.intervalo = intervalo

    def debug(self, info):
        if DEBUG:
            logging.debug(info)

    def enviar_sms(self, lista, mysql_conn):
        ids = []

        if len(lista) != 0:
            try:
                self.manager.connect(ami_login['host'])
                self.manager.login(ami_login['user'], ami_login['secret'])
                print('Manager conectado:', self.manager.connected())

                if self.manager.connected():
                    for linha in lista:
                        telefone = linha['destino']
                        mensagem = linha['mensagem']
                        comando = 'dgv send sms {} {} "{}"'.format(
                            self.grupo_portas_gsm,
                            telefone,
                            mensagem
                        )
                        self.debug('Comando: {}'.format(comando))
                        resultado = self.manager.command(comando)
                        ids.append(linha['id'])
                        self.debug(resultado.data)
                        query = "UPDATE mensagens SET enviado = 1, data_envio = '{}' WHERE id = {}".format(
                            datetime.today().strftime('%Y-%m-%d %H:%M:%S'),
                            linha['id']
                        )
                        resultado = mysql_conn.query(query)
                        mysql_conn.commit()
                        sleep(self.intervalo)
    
                self.manager.logoff()
            
            except:
                self.debug('Falha no processo')
        
        else:
            self.debug('Não existem arquivos para envio SMS')

        return ids