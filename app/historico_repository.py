import sqlite3
import database
def criarTabelaHistoricoDePreco():
    """Essa funcao sera chamada no começo da execucao para verificar se a tabela ja existe. Se não existir, irá criar"""
    database.alterarBase("""
    CREATE TABLE IF NOT EXISTS historico_de_precos(
    id_historico_preco INTEGER PRIMARY KEY AUTOINCREMENT,
    id_produto INTEGER NOT NULL,
    data_consulta TEXT NOT NULL,
    valor DOUBLE NOT NULL,
    FOREIGN KEY (id_produto) REFERENCES produto (id))""")
    # formato de data para data_consulta yyyy-mm-dd HH24:MI:SS
def inserirRegistroNoHistorico(idProduto,dataConsulta,valor):
    """Funcao utilizada para inserir os registros na tabela de historico de precos"""
    parametrosHistorico = (idProduto,dataConsulta,valor)
    database.alterarBase("""
    INSERT INTO historico_de_precos (id_produto,data_consulta,valor) VALUES(?1,?2,?3)
    """,parametrosHistorico)
def consultarTodosHistoricos():
    """Funcao utilizada para realizar uma consulta TODOS os historicos"""
    resultado = database.consultarBase("""
    SELECT produto.nome as nome_produto,historico_de_precos.* FROM historico_de_precos
    INNER JOIN produto on historico_de_precos.id_produto = produto.id                                  
    """)
    return resultado
def consultarUltimoPrecoDoProduto(idProduto):
    """Funcao utilizada para buscar o ultimo preco registrado de um produto usando o ID como criterio de busca"""
    parametroIDProduto = (idProduto,)
    resultado = database.consultarBase("""
    SELECT valor,data_consulta from historico_de_precos WHERE id_produto = ?
    ORDER BY data_consulta DESC LIMIT 1
    """,parametroIDProduto)
    return resultado
def consultarHistoricoDoProduto(idProduto):
    """Funcao utilizada para buscar o historico completo de um produto especifico"""
    parametroIDProduto = (idProduto,)
    resultado = database.consultarBase("SELECT * FROM historico_de_precos where id_produto = ?", parametroIDProduto)
    return resultado
def consultarHistoricoDoProdutoNoIntervaloDeTempo(idProduto,quantidadeMeses):
    """Funcao utilizada para consultar o historico de um produto em um periodo em meses"""
    parametroIDProduto = (idProduto,quantidadeMeses)
    resultado = database.consultarBase("""
    SELECT * FROM historico_de_precos WHERE id_produto = ?1 AND DATE(data_consulta) >= DATE('now','-'||?2|| ' month') 
    """,parametroIDProduto)
    return resultado