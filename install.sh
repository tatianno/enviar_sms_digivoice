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

cp $DIR_INSTALL/confs/samba/smb.conf /etc/samba/smb.conf
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

#Limpando arquivos desnecessarios
cd $DIR_ATUAL
rm -r enviar_sms_digivoice