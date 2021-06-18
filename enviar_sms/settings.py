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

#Formatacao do arquivo CSV
posicao_dados_csv = {
    'telefone' : 0,
    'id_movimento' : 1,
    'status' : 2,
    'mensagem' : 3
}

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
    'user' : 'gnew',
    'passwd' : 'asJeuqodk9837',
    'database' : 'envio_sms',
}
