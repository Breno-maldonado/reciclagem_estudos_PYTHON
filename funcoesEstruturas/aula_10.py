# raise NomeDoErro("mensagem_desejada")

def media(lista: list=[0]) -> float:

    calculo = sum(lista) / len(lista)

    if len(lista) > 4:
        raise ValueError("A lista não pode possuir mais do que 4 notas.")
    else:
        raise ValueError("A lista não pode possuir menos que 4 notas.")

    return calculo

notas = [5, 7, 4]
resultado = media(notas)
print(resultado)