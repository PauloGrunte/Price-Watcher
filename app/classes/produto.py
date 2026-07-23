class Produto:
    """Classe que representa um produto
        Atributos: 
        id
        url
        nome
        identificador_externo
        valor_esperado
        status 
    """
    def __init__(self,id,url,nome,identificador_externo,valor_esperado,status):
        self.id = id
        self.url = url
        self.nome = nome
        self.identificador_externo = identificador_externo
        self.valor_esperado = valor_esperado
        self.status = status