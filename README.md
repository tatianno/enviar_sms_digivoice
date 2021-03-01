# Enviar SMS através da placa VB0404GSM da DIGIVOICE
O script tem como objetivo monitorar um diretório para verificar se existem novas mensagens para enviar para o destinatário.
No exemplos estamos monitorando o diretórios arquivos.

## Formato do arquivo CSV
O arquivo CSV deve ter o seguinte formato:
```
telefone destino código de área, mensagem
telefone destino código de área, mensagem
telefone destino código de área, mensagem
telefone destino código de área, mensagem
```

## Cards instalados no asterisk
```
gnew*CLI> dgv show cards
List of available DigiVoice Cards

 Card Channels SerialNumber CardInterface        CardType     Sig.Interface IRQNumber Rsrvd Alrmd Lckd Free

    1        4 Unknown      DG_GSM_INTERFACE     VB0404GSM    GSM           16            0     0    0    4
    2       60 Unknown      DG_DIGITAL_INTERFACE VB6060PCI    R2/ISDN       20            0    60    0    0

```
