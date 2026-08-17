# Lista de listas

notas_turma = ['João', 8.0, 9.0, 10.0, 'Breno', 4.0, 6.0, 8.0, 'Lucas', 8.0, 5.0, 6.0, 'Vitor', 5.0, 5.5, 10.0, 'Thiago', 7.0, 8.0, 4.0]

nomes = []
notas_juntas = []

for i in range(len(notas_turma)):
    if i % 4 == 0:
        nomes.append(notas_turma[i])
    else:
        notas_juntas.append(notas_turma[i])

print(nomes,'\n')
print(notas_juntas)