#try:
    # codigo a ser executado
#except <nome_da_excecao as e>:
    # Se uma excecao for lançada no try e não rodar, passa para essa etapa
#else:
    # Se nenhuma for aceita, então essa
#finally:
    # Roda essa parte com ou sem excecao

notas = {'Lucas': [7.5, 8.5, 9.0], 'Mariana': [10.0, 9.5, 8.0], 'Gabriel': [6.0, 7.0, 6.5], 'Beatriz': [8.0, 8.5, 9.5], 'Carlos': [5.0, 6.0, 7.0], 'Fernanda': [9.0, 8.0, 8.5], 'Rafael': [4.5, 6.0, 5.5], 'Amanda': [7.0, 9.0, 10.0]}

try:
    nome = input("Digite o nome do(a) estudante: ")
    resultado = notas[nome]
except KeyError:
    print("Estudante não matriculado(a) na turma")
else:
    print(resultado)
finally:
    print("A consulta foi encerrada!")
