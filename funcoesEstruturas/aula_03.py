# função lambda, são funções que não precisam ser definidas, ex: lambda <variavel>: <expressão>

nota = float(input("Digite a nota do(a) estudante: "))

def qualitativo(x):
    return x + 0.5

print(qualitativo(nota))

# Lambda

notas = float(input("Digite a nota do(a) estudante: "))

qualitativos = lambda x: x + 0.5

print(qualitativos(notas))