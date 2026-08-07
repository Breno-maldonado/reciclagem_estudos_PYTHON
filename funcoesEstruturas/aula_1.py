# Funções não é nada menos do que uma sequencia de instruições que podem ser reutilizadas em diferentes partes do codigo

# Built-in functions

notas = {'1º Trimestre': 8.5, '2º Trimestre': 9.5, '3º Trimestre': 7,}
print(notas)

# Calculando a soma
soma = 0
for nota in notas.values():
    soma += nota

print(soma)

# Calculando a soma Built-in
somatorio = sum(notas.values())
print(somatorio)

# Retornar o tamanho ou o número de itens de um objeto Built-in
qtd_notas = len(notas)
print(qtd_notas)

# Calculando a média
media = somatorio / qtd_notas
print(media)

# Calculando a média Built-in
mediaRound = round(media, 1)
print(mediaRound)