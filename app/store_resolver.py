from app.webSites.Amazon import service
def storeResolver(url):
    if 'amazon' in url.lower():
        return service    
    else:
        return None