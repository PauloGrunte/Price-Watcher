from app.store_resolver import storeResolver
import app.produto_repository as produto_repository
import app.historico_repository as historico_repository
from app.verificacoes_produto_db import verificarSeProdutoExiste
import app.verificacoes_historico_db as verificacoes_historico_db
def verificarSeValorMudou(precoAtual,idExterno):
    """Essa funcao ira comparar o preco do produto usando produto_repository (preco do produto na ultima consulta) e read_scraper (preco atual), retornando um booleano"""
    ultimoPrecoNoHistorico = verificacoes_historico_db.obterUltimoPreco(idExterno)
    if float(precoAtual) != float(ultimoPrecoNoHistorico):
        return float(precoAtual) <= float(ultimoPrecoNoHistorico) # Ira retornar True/False dependendo do resultado
    else:
        return False
    
def inserirRegistroNoHistorico(dataHora,valor,idExterno):
    """Funcao utilizada para chamar historico_repository e inserir registro do produto no banco caso necessario"""
    idProduto = verificacoes_historico_db.obterUltimoPreco(idExterno=idExterno)
    historico_repository.inserirRegistroNoHistorico(idProduto=idProduto,dataConsulta=dataHora,valor=valor)
    
def montarMensagem(nome,valor):
    """Funcao utilizada para montar a mensagem que sera enviada"""
    return (f"O item {nome} esta pelo valor de: {valor}")
    
def sinalizarEnvio():
    """Essa funcao nao fara o envio mas sinalizara a funcao resposavel em enviar_mensagem para enviar. Feito dessa forma para possibilitar a incrementacao de outros meios de envio"""
    pass
def monitorarProduto(produto):
    """Funcao responsavel por orquestrar as outras funcoes de monitor_services para cada produto"""
    nome = produto['nome']
    valor = produto['preco']
    idExterno = produto['idExterno']
    datahora = produto['dataHora']
    if verificarSeValorMudou(precoAtual=valor,idExterno=idExterno):
        montarMensagem(nome=nome,valor=valor)
        inserirRegistroNoHistorico(dataHora=datahora,valor=valor,idExterno=idExterno)

def monitorService():
    """Funcao responsavel por chamar monitorarProduto(produto) para cada produto ativo"""
    TodosOsProdutos = produto_repository.listarProdutosAtivos()
    for produto in TodosOsProdutos:
        produtoInfo = storeResolver(produto['url'])
        if produtoInfo is not None:
            monitorarProduto(produtoInfo)