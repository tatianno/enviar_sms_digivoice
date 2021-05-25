#!/bin/bash
DIR_PROD='/home/tatianno/Projetos/enviar_sms_digivoice/sms/prod'
DIR_OLD='/home/tatianno/Projetos/enviar_sms_digivoice/sms/old'
DIR_SMS='/home/tatianno/Projetos/enviar_sms_digivoice/sms'
DIR_LOG='/home/tatianno/Projetos/enviar_sms_digivoice/sms.log'
QTDADE_SMS=$(/bin/ls -l $DIR_PROD/ | grep rw | wc -l)

if [ $QTDADE_SMS -gt 0 ]
    then
        #Copiando arquivos para diretorio de producao
        /bin/cp $DIR_PROD/* $DIR_SMS/
        /bin/mv $DIR_PROD/* $DIR_OLD/
        /bin/echo "$(date) $QTDADE_SMS Arquivos SMS copiados" >> $DIR_LOG
fi