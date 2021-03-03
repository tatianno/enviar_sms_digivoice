# Enviar SMS através da placa VB0404GSM da DIGIVOICE
O script tem como objetivo monitorar um diretório para verificar se existem novas mensagens para enviar para o destinatário.
Os arquivos para 

## Formato do arquivo CSV
O arquivo CSV deve ter o seguinte formato:
```
telefone destino código de área;id_movimentacao;status;mensagem
```

## Cards instalados no asterisk
```
gnew*CLI> dgv show cards
List of available DigiVoice Cards

 Card Channels SerialNumber CardInterface        CardType     Sig.Interface IRQNumber Rsrvd Alrmd Lckd Free

    1        4 Unknown      DG_GSM_INTERFACE     VB0404GSM    GSM           16            0     0    0    4
    2       60 Unknown      DG_DIGITAL_INTERFACE VB6060PCI    R2/ISDN       20            0    60    0    0

```

## Cenário utilizado
- Ubuntu Server 14.04.1
- Asterisk 1.8.31.0
- Channel Driver 1.1.8 
- VoicerLib 4.2.5.6 (4256)

## Instalação
1- Execute o script install.sh para instalação de dependências.
2- Inclua a tarefa no cron
>> `*/1 * * * *root /usr/local/enviar_sms_digivoice/enviar_sms/main.py`

## Uso
O script por padrão monitora o diretório /home/gnew/sms a cada minuto (tarefa automatizada no crontab).
O diretório pode ser montado via smbd.