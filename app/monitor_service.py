from app.store_resolver import storeResolver
import app.produto_repository as produto_repository
import app.historico_repository as historico_repository
import app.verificacoes_historico_db as verificacoes_historico_db
from app.classes.produto import Produto
from app.classes.produtoConsultaWeb import ProdutoConsultaWeb
import logging
logger = logging.getLogger(__name__)
def verificarSeValorMudou(precoAtual,idProduto):
    """Essa funcao ira comparar o preco do produto usando produto_repository (preco do produto na ultima consulta) e read_scraper (preco atual), retornando um booleano"""
    ultimoPrecoNoHistorico = verificacoes_historico_db.obterUltimoPreco(idProduto)
    return float(precoAtual) != float(ultimoPrecoNoHistorico) # Ira retornar True/False dependendo do resultado
def verificarSeValorEhMenor(precoAtual,idProduto):
    """Essa funcao ira comparar o preco do produto usando produto_repository (preco do produto na ultima consulta) e read_scraper (preco atual) para saber se o valor diminuiu, retornando um booleano"""
    ultimoPrecoNoHistorico = verificacoes_historico_db.obterUltimoPreco(idProduto)
    return float(precoAtual) < float(ultimoPrecoNoHistorico) # Ira retornar True/False dependendo do resultado
def montarObjetoProduto(produtoListado):
    """Essa funca recebe um produto no molde dict e retorna o objeto Produto"""
    objetoProduto = Produto(id=produtoListado['id'],url=produtoListado['url'],nome=produtoListado['nome'],identificador_externo=produtoListado['identificador_externo'],valor_esperado=produtoListado['valor_esperado'],status=produtoListado['status'])
    return objetoProduto

def inserirRegistroNoHistorico(idProduto,dataHora,valor):
    """Funcao utilizada para chamar historico_repository e inserir registro do produto no banco caso necessario"""
    historico_repository.inserirRegistroNoHistorico(idProduto=idProduto,dataConsulta=dataHora,valor=valor)
  
def montarMensagem(nome,valor):
    """Funcao utilizada para montar a mensagem que sera enviada"""
    return (f"O item {nome} esta pelo valor de: {valor}")
    
def sinalizarEnvio():
    """Essa funcao nao fara o envio mas sinalizara a funcao resposavel em enviar_mensagem para enviar. Feito dessa forma para possibilitar a incrementacao de outros meios de envio"""
    pass
def monitorarProduto(produto):
    """Funcao responsavel por orquestrar as outras funcoes de monitor_services para cada produto"""
    try: 
        service = storeResolver(produto.url)
        if service != None:
            produtoConsultaWeb = service.obterDadosProduto(produto.url)
            if produtoConsultaWeb != None:
                objetoProdutoConsultaWeb = ProdutoConsultaWeb(nome=produtoConsultaWeb['nome'],preco=produtoConsultaWeb['preco'],identificadorExterno=produtoConsultaWeb['idExterno'],dataHora=produtoConsultaWeb['dataHora'])
                if verificarSeValorMudou(precoAtual=objetoProdutoConsultaWeb.preco,idProduto=produto.id):
                    inserirRegistroNoHistorico(idProduto=produto.id,dataHora=objetoProdutoConsultaWeb.dataHora,valor=objetoProdutoConsultaWeb.preco)
                if verificarSeValorEhMenor(precoAtual=objetoProdutoConsultaWeb.preco,idProduto=produto.id):
                    montarMensagem()
            else: 
                logging.info(f"Não foi possivel obter dados do produto: {produto.nome}")
        else:
            pass
    except:
        pass

def monitorService():
    """Funcao responsavel por chamar monitorarProduto(produto) para cada produto ativo"""
    TodosOsProdutos = produto_repository.listarProdutosAtivos()
    for produtoListado in TodosOsProdutos:
        #print(produto)
        objetoProduto = montarObjetoProduto(produtoListado)
        monitorarProduto(objetoProduto)
monitorService()