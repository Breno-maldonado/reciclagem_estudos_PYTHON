# Map, serve para conseguirmos utilizar o lambda + variaveis no mesmo valor


qualitativo = lambda x: x + 0.5
notas = [5.0, 8.0, 5.5, 9.0]

notas_atualizadas = list(map(qualitativo, notas))

print(notas_atualizadas)
print(notas)