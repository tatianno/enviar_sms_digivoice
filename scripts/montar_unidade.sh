#!/bin/bash
USERNAME='gnew'
PWD='XXXX'
CAMINHO='//teste.local/dados/'

/sbin/mount.cifs $CAMINHO /media/sms -o username=$USERNAME,password=$PWD
