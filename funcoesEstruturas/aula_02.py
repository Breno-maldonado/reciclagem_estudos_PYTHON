# para criar funções você utiliza o def <nome>():
#                                       <instrucoes>

def media():
    calculo = (10 + 9 + 8) / 3
    print(calculo)

media()

# tambem podemos adicionar parametros nas funções
def medias(nota_1, nota_2, nota_3):
    calculos = (nota_1 + nota_2 + nota_3)
    print(calculos)

medias(2, 4, 6)

# utilizando a função
nota1 = 5
nota2 = 5
nota3 = 2
medias(nota1, nota2, nota3)