import sqlite3
from functools import wraps
import app.config as config
import logging
#logging.basicConfig(filename=config.logPath,level=logging.INFO,format='%(asctime)s - %(levelname)s - %(message)s')
def conexaoBanco(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
     try:
        #logging.info("[database] Abrindo conexao com o banco")   
        con = sqlite3.connect(config.DBPath) # Criando a conexão com o banco e utilizando ../ para nao utilizar o caminho completo
        con.row_factory = sqlite3.Row # Hbailitando o acesso pelo nome da coluna. Será util para transformar a saida em um dict
        cur = con.cursor() # Criando o Cursor responsável pelas interações com o banco SQLLITE
        kwargs['con'] = con
        kwargs['cur'] = cur
        return func(*args, **kwargs)
     except:
        pass
        #logging.exception("[database] Erro ao conectar no banco")
     finally:
        con.close()
    return wrapper    
@conexaoBanco
def alterarBase(texto,parametros=(),con = None,cur = None):
  """Funcao utilizada para alterar/inserir dados no banco"""
  cur.execute(texto,parametros)
  con.commit() # commit utilizado para gravar alteracoes
@conexaoBanco
def consultarBase(texto,parametros=(),con = None,cur = None):
  """Funcao utilizada para consultar o banco"""
  # ausencia de commit para evitar edicoes no banco com essa funcao 
  cur.execute(texto,parametros)
  dictRes = [dict(row) for row in cur.fetchall()]
  return dictRes