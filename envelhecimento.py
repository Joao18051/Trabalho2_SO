class envelhecimento(molduras, chamadaPaginas):
    def __init__(self, molduras, chamadaPaginas):
        self.molduras = molduras
        self.chamadaProcessos = chamadaPaginas

        self.faltasPagina = 0
        #Matriz vazia de 1 coluna e 4 linhas vazias, fazer cada linha ter tamanho de 8 colunas, 
        #para representar os 8 ciclos de clock de observação, preenche-los com 0s.
        self.contador = [[[] for _ in range(molduras)]]

    def start(self):
        #Criar molduras

        

chamadaPaginas = [] #Testar o código com a ordem de chamadas da referenciaPagina1.txt e referenciaPagina1.txt
molduras = 4
e = envelhecimento(molduras, chamadaPaginas)
e.start()