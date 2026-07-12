from webSites.Amazon.parse import parse
from webSites.Amazon.client import scraper
import logging
import config
def receberHTMLDoScraper(url):
    htmlPagina = scraper(url)
    return htmlPagina
def obterDadosProduto(url):
    htmlPagina = receberHTMLDoScraper(url)
    dadosProduto = parse(url=url,htmlPagina=htmlPagina)
    return dadosProduto
obterDadosProduto("https://www.amazon.com.br/English-Everyone-Practice-Level-Beginner/dp/0744098572")