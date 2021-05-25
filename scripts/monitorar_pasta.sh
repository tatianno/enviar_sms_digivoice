#!/bin/bash
DIR_PROD='/media/sms/StatusPedidosSMS'
DIR_OLD='/home/gnew/old'
DIR_SMS='/home/gnew/sms'
DIR_LOG='/home/gnew/sms.log'
QTDADE_SMS=$(/bin/ls -l $DIR_PROD/ | grep rw | wc -l)

if [ $QTDADE_SMS -gt 0 ]
    then
        #Copiando arquivos para diretorio de producao
        /bin/cp $DIR_PROD/* $DIR_SMS/
        /bin/mv $DIR_PROD/* $DIR_OLD/
        /bin/echo "$(date) $QTDADE_SMS Arquivos SMS copiados" >> $DIR_LOG
fi