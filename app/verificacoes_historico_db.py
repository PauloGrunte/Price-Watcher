import app.historico_repository as historico_repository
import app.verificacoes_produto_db as verificacoes_produto_db
def obterUltimoPreco(idExterno):
    idProduto = verificacoes_produto_db.obterIDProduto(identificadorExterno=idExterno)
    ultimoPreco = historico_repository.consultarUltimoPrecoDoProduto(idProduto)[0]['valor']
    return ultimoPreco
