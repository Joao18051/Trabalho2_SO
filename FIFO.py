import ast


class FIFO:
    def __init__(self, molduras, chamadaPaginas):
        self.molduras = molduras
        self.chamadaPaginas = chamadaPaginas
        self.faltasPagina = 0
        self.frames = []  # as molduras
        self.top = 0

    def start(self):
        print("Referencia | Moldura →\t", end='')
        for i in range(self.molduras):
            print(f' {i}', end=' ')
        print("Fault\n   ↓\n")

        for pagina in self.chamadaPaginas:
            if pagina not in self.frames:
                if len(self.frames) < self.molduras:
                    self.frames.append(pagina)
                else:
                    self.frames[self.top] = pagina
                    self.top = (self.top + 1) % self.molduras
                self.faltasPagina += 1
                pf = 'falta de página'
            else:
                pf = 'Está na memória'

            print(f"   {pagina}\t\t", end='')
            for x in self.frames:
                print(f' {x}', end=' ')
            for _ in range(self.molduras - len(self.frames)):
                print('   ', end=' ')
            print(f" {pf}")

        print("\nNúmero de requests: %d" % len(self.chamadaPaginas))
        print("Número de faltas de páginas: %d" % self.faltasPagina)
        print("Taxa de falta de página: %0.2f%%" % ((self.faltasPagina / len(self.chamadaPaginas)) * 100))


def carregarReferencias(arquivo):
    with open(arquivo, 'r') as file:
        conteudo = file.read().strip()
    referencias = ast.literal_eval(conteudo)
    return referencias


referencia = 'referenciaPagina1.txt'
chamadaPaginas = carregarReferencias(referencia)
molduras = 4
e = FIFO(molduras, chamadaPaginas)
e.start()

referencia2 = 'referenciaPagina2s.txt'
chamadaPaginas2 = carregarReferencias(referencia2)
f = FIFO(molduras, chamadaPaginas2)
f.start()
