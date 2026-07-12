#import scraper
from bs4 import BeautifulSoup
import logging
#import config
import datetime
logger = logging.getLogger(__name__)
"""Read Scraper - Amazon"""
def obterPrecoWeb(htmlPagina):
    logger.info("[Parse Amazon] Extraindo preco")
    precoProdutoContainerSuperior = htmlPagina.find('div', id='corePriceDisplay_desktop_feature_div')
    try:
        precoParteInteira = precoProdutoContainerSuperior.find('span',class_="a-price-whole") #Retorna a parte inteira do valor (Parte antes da virgula)
        precoParteDecimal = precoProdutoContainerSuperior.find('span', class_="a-price-fraction") #Retorna a parte decimal do valor (Parte depois da virgula)
        precoProduto = str(precoParteInteira.text) + str(precoParteDecimal.text) #Concatenando os valores para formar o valor total
        precoProduto = precoProduto.replace(",",".") #Trocando , por . para poder usar como Double
        return precoProduto
    except:
        logger.exception("[Parse Amazon] Erro ao extrair o preco")
        return None
def obterNomeProdutoWeb(htmlPagina):
    try:
        logger.info("[Parse Amazon] Obtendo nome do produto")
        nomeProdutoContainerSuperior = htmlPagina.find('div',id='titleSection')
        nomeProduto = nomeProdutoContainerSuperior.find('span',id="productTitle")
        nomeProduto = nomeProduto.text
        return nomeProduto
    except:
        logger.exception("[Parse Amazon] Erro ao obter nome do Produto")
        return None
def obterIDExternoWeb(url):
    try:
        logger.info("[Parse Amazon] Obtendo ID externo do produto")
        idExternoASIN = url.split('/dp/')
        idExternoASIN = idExternoASIN[1][:10]
        return idExternoASIN
    except:
        logger.exception("[Parse Amazon] Erro ao obter ID externo do produto")
        return None
def obterDataHora(): # Utilizado para obter DataHora da consulta no WebSite
    dataHora = datetime.datetime.now()
    dataHora = dataHora.strftime("%Y/%m/%d %H:%M:%S")
    return dataHora
def montarDadosProdutoWeb(precoProduto,nomeProduto,IDExternoProduto,dataHora):
    produto = {
        'nome': nomeProduto,
        'preco': precoProduto,
        'idExterno':IDExternoProduto,
        'dataHora': dataHora }
    return produto
def parse(url,htmlPagina):
    precoProduto = obterPrecoWeb(htmlPagina)
    nomeProduto = obterNomeProdutoWeb(htmlPagina)
    IDExternoProduto = obterIDExternoWeb(url)
    dataHora = obterDataHora()
    if precoProduto is not None and nomeProduto is not None and IDExternoProduto is not None and dataHora is not None:
        produto = montarDadosProdutoWeb(precoProduto=precoProduto,nomeProduto=nomeProduto,IDExternoProduto=IDExternoProduto,dataHora=dataHora)
        return produto