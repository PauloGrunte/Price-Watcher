from app.webSites.Amazon.parse import parse
from app.webSites.Amazon.client import scraper
import logging
logger = logging.getLogger(__name__)
def receberHTMLDoScraper(url):
    htmlPagina = scraper(url)
    return htmlPagina
def obterDadosProduto(url):
    htmlPagina = receberHTMLDoScraper(url)
    if htmlPagina != None:
        dadosProduto = parse(url=url,htmlPagina=htmlPagina)
        return dadosProduto
    else:
        logger.error("Erro ao extrair os dados do produto")
        return None