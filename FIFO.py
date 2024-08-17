class FIFO(molduras, chamadaPaginas):
    def __init__(self, molduras, chamadaPaginas):
        self.molduras = molduras
        self.chamadaProcessos = chamadaPaginas

        self.faltasPagina = 0

    def start(self):
        #Criar molduras
        

chamadaPaginas = [] #Testar o código com a ordem de chamadas da referenciaPagina1.txt e referenciaPagina1.txt
molduras = 4
e = FIFO(molduras, chamadaPaginas)
e.start()