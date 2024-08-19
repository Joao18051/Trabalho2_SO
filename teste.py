import ast

class Envelhecimento:
    def __init__(self, molduras, chamadaPaginas, n_bits=8):
        self.molduras = molduras
        self.chamadaPaginas = chamadaPaginas
        self.faltasPagina = 0
        self.frames = {}  # Dicionário para armazenar as páginas e suas idades
        self.n_bits = n_bits  # Número de bits para o contador de idade

    def start(self):
        print("Referencia | Moldura →\t", end='')
        for i in range(self.molduras):
            print(f' {i}', end=' ')
        print("Fault\n   ↓\n")

        for pagina in self.chamadaPaginas:
            # Atualizar as idades de todas as páginas em molduras (right shift)
            for key in self.frames:
                self.frames[key] >>= 1

            if pagina not in self.frames:
                self.faltasPagina += 1
                if len(self.frames) < self.molduras:
                    # Adiciona a nova página com o bit mais significativo ativado
                    self.frames[pagina] = 1 << (self.n_bits - 1)
                else:
                    # Substituir a página com o menor valor de idade
                    pagina_a_substituir = min(self.frames, key=self.frames.get)
                    del self.frames[pagina_a_substituir]
                    self.frames[pagina] = 1 << (self.n_bits - 1)
                pf = 'falta de página'
            else:
                # Se a página já está em moldura, atualiza o bit mais significativo
                self.frames[pagina] |= 1 << (self.n_bits - 1)
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
e = Envelhecimento(molduras, chamadaPaginas)
e.start()

referencia2 = 'referenciaPagina2s.txt'  # Usando o mesmo arquivo para testar
chamadaPaginas2 = carregarReferencias(referencia2)
f = Envelhecimento(molduras, chamadaPaginas2)
f.start()

print("aging")