import app.produto_repository as produto_repository
def verificarSeProdutoExiste(id = None,nome = None, identificadorExterno = None):
    if produto_repository.consultarProduto(id=id,nome=nome,identificadorExterno=identificadorExterno) is not None:
        return True
    else:
        return False
def obterIDProduto(id = None,nome = None, identificadorExterno = None):
    idProduto = produto_repository.consultarProduto(id=id,nome=nome,identificadorExterno=identificadorExterno)[0]['id']
    return idProduto    