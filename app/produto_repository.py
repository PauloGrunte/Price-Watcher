import sqlite3
import app.database as database
def criarTabelaProduto():
    """Essa funcao sera chamada no começo da execucao para verificar se a tabela ja existe. Se não existir, irá criar"""
    database.alterarBase("""
    CREATE TABLE IF NOT EXISTS produto(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    url STRING NOT NULL,
    nome STRING,
    identificador_externo STRING NOT NULL,
    valor_esperado DOUBLE,
    status BOOL)""")
def inserirProduto(url,nome,identificadorExterno,valorEsperado):
    """Funcao Utilizada para inserir produtos na base"""
    parametrosProduto = (url,nome,identificadorExterno,valorEsperado)
    database.alterarBase("""
    INSERT INTO produto (url,nome,identificador_externo,valor_esperado,status) 
    VALUES (?,?,?,?,'T')""",parametrosProduto)
def inativarProduto(id):
    """"Funcao utilizada para sinalizar os produtos inativos"""
    parametroID = (id,)
    database.alterarBase("""
    UPDATE produto set 
    status = 'F' WHERE id = ?
    """,parametroID)
def reativarProduto(id):
    """"Funcao utilizada para reativar produtos"""
    parametroID = (id,)
    database.alterarBase("""
    UPDATE produto set 
    status = 'T' WHERE id = ?
    """,parametroID)
def consultarProduto(id = None,nome = None, identificadorExterno = None):
    """Consulta SQL para consultar apenas um produto"""
    nomeUpperCase = nome.upper() if nome is not None else None
    parametrosProduto = (id,nomeUpperCase,identificadorExterno)
    resultado = database.consultarBase("""
    SELECT * FROM produto WHERE (?1 is NULL or id = ?1) 
    and (?2 is NULL or upper(nome) LIKE '%' || ?2 || '%')
    and (?3 is NULL or identificador_externo = ?3)
""",parametrosProduto)
    return resultado
def listarProdutosAtivos():
    """Consulta SQL para trazer todos os produtos ativos"""
    resultado = database.consultarBase("SELECT * from produto WHERE status = 'T'")
    return resultado
def listarTodosOsProdutos():
    """Consulta SQL para trazer todos os produtos cadastrados"""
    resultado = database.consultarBase("SELECT * from produto")
    return resultado
