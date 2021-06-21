#Modo Debug
DEBUG = True
#log_file = '/var/log/enviar_sms.log'
log_file = '/home/tatianno/Projetos/enviar_sms_digivoice/enviar_sms.log'
#Diretorio monitorado com os arquivos csv com destino e mensagem do SMS
#pasta_mensagens = '/home/gnew/sms'
pasta_mensagens = '/home/tatianno/Projetos/enviar_sms_digivoice/sms/prod'

#Extensoes aceitas
extensoes_validas = ['txt', 'csv']

#Delimitador do arquivo CSV
delimitador = ';'

#Dados do AMI
ami_login = {
    'host' : '127.0.0.1',
    'user' : 'user',
    'secret' : 'passwd',
}

#Grupo com as portas GSM configurado no digivoice.conf
grupo_portas_gsm = 'g1'

#Dados para conexao com banco de dados
db = {
    'host' : 'localhost',
    'user' : 'sms',
    'passwd' : 'asJeuqo',
    'database' : 'envio_sms',
}

intervalo_verificacoes = 300