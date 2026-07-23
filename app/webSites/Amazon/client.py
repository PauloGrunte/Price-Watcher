"""Client Amazon - Responsavel por"""
from bs4 import BeautifulSoup
from html.parser import HTMLParser
import logging
from curl_cffi import requests
logger = logging.getLogger(__name__)
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
    'Accept-Language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-User': '?1'
}
def scraper(url):
    """Essa funcao sera responsavel por obter os dados da pagina web atraves da URL passada para ela"""
    try: 
        logger.info(f"[Scraper] Enviando request para URl - {url}")
        #response = requests.get(url,headers=headers)
        session = requests.Session(impersonate="chrome120")
        session.get("https://www.amazon.com.br/")
        response = session.get(url)
    except:
        response = None 
        logger.exception(f"[Scraper] erro ao enviar request para a URL - {url}")
    if(response != None):
        #soup = BeautifulSoup(response.text,'html.parser') #criando o objeto soup para receber os dados da pagina web
        soup = BeautifulSoup(response.content, "html.parser") 
        if(soup.find('body') is not None):
            logger.info("[Scraper] sucesso ao criar o objeto.")
            return soup
        logger.error("[Scraper] retornando None pois o objeto nao pode ser criado")
    return None