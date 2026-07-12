import produto_repository
import historico_repository
import read_scraper
import enviar_mensagem
def verificarSeValorMudou():
    """Essa funcao ira comparar o preco do produto usando produto_repository (preco do produto na ultima consulta) e read_scraper (preco atual), retornando um booleano"""
    pass
def inserirRegistroNoHistorico():
    """Funcao utilizada para chamar historico_repository e inserir registro do produto no banco caso necessario"""
    pass
def montarMensagem():
    """Funcao utilizada para montar a mensagem que sera enviada"""
    pass
def sinalizarEnvio():
    """Essa funcao nao fara o envio mas sinalizara a funcao resposavel em enviar_mensagem para enviar. Feito dessa forma para possibilitar a incrementacao de outros meios de envio"""
    pass
def monitorarProduto(produto):
    """Funcao responsavel por orquestrar as outras funcoes de monitor_services para cada produto"""
def monitorService():
    """Funcao responsavel por chamar monitorarProduto(produto) para cada produto ativo"""
    pass