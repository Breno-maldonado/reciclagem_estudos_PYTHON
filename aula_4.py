st = "Duplas"
st1 = 'Simples'
# As strings podem contem tanto aspas duplas como apenas simples, o resultado é o mesmo

st2 = 'Aspas dentro de "apapas"'
# E também podem ficar dentro delas mesmas, uma ficando fora duplas ou simples e dentro mantendo a inversa
st3 = "Desse 'jeito'"

# para utilizarmos alguns metodos em strings, ele segue um padrão (objeto.metodo())

#str  objeto string
#upper()  deixa a string maiuscula
# para unir utilizamos o ponto "."

texto = "essa frase ficara maiuscula"
print(str.upper(texto),'\n')

# do contrario, para diminuir utilizamos o lower()

texto2 = "ESSA FRASE FICARA MINUSCULA"
print(str.lower(texto2),'\n')

# para removermos espaços em branco no inicio e no fim de uma string, podemos utilizar o strip()

texto3 = " essa frase contem espaços "
print(str.strip(texto3),'\n')

# para substituirmos textos podemos utilizar o replace(x,y) x=antigo e y=novo

texto4 = "essa frase foi substituida"
print(texto4.replace('substituida', 'modificada'))