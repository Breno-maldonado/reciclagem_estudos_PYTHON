# 6) Escreva um programa que peça uma data informando o dia, mês e ano e determine se ela é válida para uma análise.

dia = int(input("Digite o dia: "))
mes = int(input("Digite o número do mês: "))
ano = int(input("Digite o ano: "))

if dia >= 32:
    print("O dia não condiz com o calendario")
elif mes >= 13:
    print("O mês não condiz com o calendario")
elif ano < 2026 or ano >= 2027:
    print("O ano não condiz com o calendario atual")

print(f"{dia}/{mes}/{ano}")
