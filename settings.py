#Diretorio monitorado com os arquivos csv com destino e mensagem do SMS
pasta_mensagens = 'arquivos'

#Formatacao do arquivo CSV
posicao_dados_csv = {
    'telefone' : 0,
    'mensagem' : 1
}

#Dados do AMI
ami_login = {
    'host' : '127.0.0.1',
    'user' : 'user',
    'secret' : 'passwd',
}

#Grupo com as portas GSM configurado no digivoice.conf
grupo_portas_gsm = 'g1'