from app.webSites.Amazon.service import obterDadosProduto
def storeResolver(url):
    if 'amazon' in url.lower():
        return obterDadosProduto(url)     
    else:
        return "Outra loja" 