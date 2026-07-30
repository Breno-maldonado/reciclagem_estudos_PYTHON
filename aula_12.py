# ainda sobre manipulação de listas, temos o append() que adiciona um elemento ao final da lista

lista = ['Breno', 'Ana', 'Malu']
lista.append('Jade')
print(lista)

# temos tambem o extend() que adiciona varios elementos ao final da lista

notas = ['Breno', 4.2]
notas.extend([10.0,7.5,9.0])
print(notas)

# temos tambem o remove() que remove elementos da lista

sobrenome = ['Maldonado', 'Rodrigues', 'Alves']
sobrenome.remove('Alves')
print(sobrenome)