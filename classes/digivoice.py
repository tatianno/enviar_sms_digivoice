from asterisk.manager import Manager
from settings import ami_login
from settings import posicao_dados_csv

class Digivoice():

    def __init__(self, grupo_portas_gsm='g1'):
        self.grupo_portas_gsm = grupo_portas_gsm
        self.manager = Manager() 

    def enviar_sms(self, lista):
        if len(lista) != 0:
            self.manager.connect(ami_login['host'])
            self.manager.login(ami_login['user'], ami_login['secret'])

            for linha in lista:
                if len(posicao_dados_csv) == len(linha):
                    telefone = linha[posicao_dados_csv['telefone']]
                    mensagem = linha[posicao_dados_csv['mensagem']]
                    comando = 'dgv send sms {} {} "{}"'.format(
                        self.grupo_portas_gsm,
                        telefone,
                        mensagem
                    )
                    resultado = self.manager.command(comando)
                    print(resultado)
            
            self.manager.logoff()
            self.manager.close()