#!/bin/bash
DIR_INSTALL="/usr/local/enviar_sms_digivoice"
DIR_SHARE="/home/gnew"
DIR_ATUAL=$(pwd)

apt-get update
apt-get install python3.4-venv python3.4-dev samba libsmbclient libsmbclient-dev libtevent0 libtalloc2 git

git clone https://github.com/tatianno/enviar_sms_digivoice.git
cp -a enviar_sms_digivoice $DIR_INSTALL

#Configuracao SMB
if [ ! -d $DIR_SHARE ];then
    echo "Criando diretorio compartilhado" 
    mkdir $DIR_SHARE
fi

if [ ! -d $DIR_SHARE/sms ];then
    echo "Criando diretorio compartilhado" 
    mkdir $DIR_SHARE/sms
fi

if [ ! -d $DIR_SHARE/old ];then
    echo "Criando diretorio para salvar sms enviados" 
    mkdir $DIR_SHARE/old
fi

if [ ! -d /media/sms ];then
    echo "Criando diretorio sms - ponto de montagem" 
    mkdir /media/sms
fi

cp $DIR_INSTALL/confs/samba/smb.conf /etc/samba/smb.conf
chown -R gnew:root $DIR_SHARE/sms/
service smbd restart

#Configuracoes asterisk
cp $DIR_INSTALL/confs/asterisk/* /etc/asterisk/
service asterisk restart

#Configurando VENV
cd $DIR_INSTALL
python3 -m venv enviar_sms/venv
source enviar_sms/venv/bin/activate
pip install -r requirements.txt

#Configurando serviço
cp services/enviar_sms /etc/init.d/
update-rc.d enviar_sms defaults

#CRIANDO BANCO DE DADOS
echo "Configurando MYSQL"
mysql -u root -e "create database envio_sms"
mysql -u root -e "CREATE USER 'sms'@'localhost' IDENTIFIED BY 'asJeuqo'"
mysql -u root -e "GRANT ALL PRIVILEGES ON envio_sms.* TO sms@localhost"
mysql -u root -e "flush privileges"
mysql -u root envio_sms < sql/envio_sms.sql

#Limpando arquivos desnecessarios
cd $DIR_ATUAL
rm -r enviar_sms_digivoice