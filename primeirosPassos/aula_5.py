# para conseguirmos coletar dados, temos alguns metodos e um deles é o input()

nome = input("Digite seu nome: ")

print("Nome: ",nome)

# tambem podemos passar os tipos de dados que serão armazenados, o input() por padrão sempre sera uma string

idade = int(input("Digite sua idade: "))

print("Idade: ",idade)

altura = float(input("Digite sua altura em metros: "))

print("Altura: ",altura)

confirmacao = bool(input("Pressione Enter para cancelar ou digite qualquer coisa para continuar: "))

if confirmacao:
    print("Continuando...")
else:
    print("Operação cancelada.")