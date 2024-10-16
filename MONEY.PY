import requests
import json

cotacoes = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")
cotacoes = cotacoes.json()
cotacao_dolar = cotacoes['USDBRL'] ["bid"]
cotacao_euro = cotacoes['EURBRL'] ["bid"]
cotacao_btc = cotacoes['BTCBRL'] ["bid"]
#print(cotacoes)
print(cotacao_btc, cotacao_dolar, cotacao_euro)


# esse codigo busca a cotação do DOLAR, EURO e do BITCOIN, convertido para o BRL real brasileiro em tempo real#
# tentar incluir outras moedas #
