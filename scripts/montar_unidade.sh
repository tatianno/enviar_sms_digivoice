#!/bin/bash
USERNAME='gnew'
PWD='Novo2021'
CAMINHO='//singular.local/dados/StatusPedidosSMS/'

/bin/mount -o username=$USERNAME,password=$PWD $CAMINHO /media/sms
