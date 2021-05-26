import logging
from time import sleep
from unicodedata import normalize
from asterisk.manager import Manager
from settings import ami_login, posicao_dados_csv, DEBUG, log_file

logging.basicConfig(
    level=logging.DEBUG, 
    filename=log_file,
    format='%(asctime)s :: %(levelname)s :: %(message)s'
)

class Digivoice():

    def __init__(self, grupo_portas_gsm='g1'):
        self.grupo_portas_gsm = grupo_portas_gsm
        self.manager = Manager()

    def debug(self, info):
        if DEBUG:
            logging.debug(info)

    def enviar_sms(self, lista):

        if len(lista) != 0:
            try:
                self.manager.connect(ami_login['host'])
                self.manager.login(ami_login['user'], ami_login['secret'])

                for linha in lista:
                    if len(posicao_dados_csv) == len(linha):
                        telefone = linha[posicao_dados_csv['telefone']]
                        mensagem = linha[posicao_dados_csv['mensagem']]
                        mensagem = normalize('NFKD', mensagem).encode('ASCII', 'ignore').decode('ASCII')
                        comando = 'dgv send sms {} {} "{}"'.format(
                            self.grupo_portas_gsm,
                            telefone,
                            mensagem
                        )
                        self.debug('Comando: {}'.format(comando))
                        resultado = self.manager.command(comando)
                        self.debug(resultado.data)
                        sleep(10)
                
                self.manager.logoff()
            
            except:
                self.debug('Falha na execução do script')
                self.debug(lista)
        
        else:
            self.debug('Não existem arquivos para envio SMS')