#!/bin/bash
USERNAME='gnew'
PWD='Novo2021'
CAMINHO='//singular.local/dados/'

/sbin/mount.cifs $CAMINHO /media/sms -o username=$USERNAME,password=$PWD
