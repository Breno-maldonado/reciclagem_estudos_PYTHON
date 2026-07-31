# 2) Com os mesmos dados da questão anterior, defina quantas compras foram realizadas acima de 3000 reais e calcule a 
# porcentagem quanto ao total de compras.

gastos = [2172.54, 3701.35, 3518.09, 3456.61, 3249.38, 2840.82, 3891.45, 3075.26, 2317.64, 3219.08]
media = sum(gastos) / len(gastos)
print(media)

acima = 0

for gasto in gastos:
    if gasto > 3000:
        acima += 1

porcentagem = (acima / len(gastos)) * 100
print(porcentagem)