from app.webSites.Amazon.parse import parse
from app.webSites.Amazon.client import scraper
import logging
def receberHTMLDoScraper(url):
    htmlPagina = scraper(url)
    return htmlPagina
def obterDadosProduto(url):
    htmlPagina = receberHTMLDoScraper(url)
    dadosProduto = parse(url=url,htmlPagina=htmlPagina)
    return dadosProduto