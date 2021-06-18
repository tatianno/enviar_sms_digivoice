import logging
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

    def enviar_sms(self, lista):
        ids = []

        if len(lista) != 0:
            try:
                self.manager.connect(ami_login['host'])
                self.manager.login(ami_login['user'], ami_login['secret'])
                self.manager_connect = True
            
            except:
                self.debug('Falha na conexão com o Asterisk')

            for linha in lista:
                telefone = linha['destino']
                mensagem = linha['mensagem']
                comando = 'dgv send sms {} {} "{}"'.format(
                    self.grupo_portas_gsm,
                    telefone,
                    mensagem
                )
                self.debug('Comando: {}'.format(comando))

                try:
                    resultado = self.manager.command(comando)
                    self.debug(resultado.data)
                
                except:
                    self.debug('Falha dgv send sms')
                
                if self.manager_connect:
                    sleep(self.intervalo)
                    ids.append(linha['id'])

            try:    
                self.manager.logoff()
            
            except:
                self.debug('Falha em desconectar do Asterisk')
        
        else:
            self.debug('Não existem arquivos para envio SMS')

        return ids