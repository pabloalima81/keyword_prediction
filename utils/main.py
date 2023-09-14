from datetime import datetime
from pytrends.request import TrendReq

def consulta_palavra(palavras_chave):
    current_date = datetime.today().strftime("%Y-%m-%d")
    
    # Crie uma instância do TrendReq
    pytrends = TrendReq(hl='pt-BR', tz=360)  # 'hl' é o idioma, 'tz' é a zona de tempo

    # Crie um payload da consulta
    pytrends.build_payload(palavras_chave, timeframe='2022-01-01 ' + current_date, geo='BR')  # 'timeframe' define o intervalo de tempo, 'geo' define a localização (Brasil)

    # Obtenha os dados de tendência
    dados_tendencia = pytrends.interest_over_time()
    return dados_tendencia

def keyword_prediction (keyword):
    word_prediction = consulta_palavra(keyword)    
    return word_prediction