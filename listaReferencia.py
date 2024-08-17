import random 
ordemPaginas = []
#Gera uma ordem de páginas de 0 à 10
while len(ordemPaginas) < 1000:
    ordemPaginas.append(random.randint(0,10)) 

f = open("referenciaPagina2s.txt", "w")

for i in range(len(ordemPaginas)):
    if i == 0:
         f.write("[")
    
    f.write('%d' % ordemPaginas[i])

    if i == len(ordemPaginas) -1:
         f.write("]")
    else:
        f.write(", ")
f.close()