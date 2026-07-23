class ProdutoConsultaWeb:
    """Classe que representa uma consulta Web
        Atributos: 
         nome
         preco
         idExterno
         dataHora
    """
    def __init__(self,nome,preco,identificadorExterno,dataHora):
        self.nome = nome
        self.preco = preco
        self.identificadorExterno = identificadorExterno
        self.dataHora = dataHora