from asterisk.manager import Manager
from settings import ami_login
from settings import posicao_dados_csv
from settings import DEBUG

class Digivoice():

    def __init__(self, grupo_portas_gsm='g1'):
        self.grupo_portas_gsm = grupo_portas_gsm
        self.manager = Manager()

    def debug(self, info):
        if DEBUG:
            print(info)

    def enviar_sms(self, lista):
        self.debug('Lista: {}'.format(str(lista)))
        
        if len(lista) != 0:
            self.debug('Conectando no AMI')
            self.manager.connect(ami_login['host'])
            self.manager.login(ami_login['user'], ami_login['secret'])

            for linha in lista:
                if len(posicao_dados_csv) == len(linha):
                    telefone = linha[posicao_dados_csv['telefone']].encode('utf-8')
                    mensagem = linha[posicao_dados_csv['mensagem']].encode('utf-8')
                    self.debug('Telefone: {}'.format(telefone))
                    self.debug('Mensagem: {}'.format(mensagem))
                    comando = 'dgv send sms {} {} "{}"'.format(
                        self.grupo_portas_gsm,
                        telefone,
                        mensagem
                    )
                    self.debug('Comando: {}'.format(comando))
                    resultado = self.manager.command(comando)
                    self.debug(resultado.data)
            
            self.debug('Desconectando no AMI')
            self.manager.logoff()
            self.manager.close()
    
        self.debug('Finalizado')