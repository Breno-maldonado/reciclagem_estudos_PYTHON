# temos alguns operadores logicos, como AND, OR, NOT e IN

t1 = t2 = True
f1 = f2 = False

# and (variavel E a outra variavel)
if t1 and t2:
    print("É verdadeira")
else:
    print("É falsa")

if t1 and f1:
    print("É verdadeira")
else:
    print("É falsa")

# or (uma variavel OU a outra variavel)
if t1 or t2:
    print("É verdadeira")
else:
    print("É falsa")

if t1 or f1:
    print("É verdadeira")
else:
    print("É falsa")

# not (variavel NÃO for...)
if not t1:
    print("É verdadeira")
else:
    print("É falsa")

if not f1:
    print("É verdadeira")
else:
    print("É falsa")

# in (valida se um valor contem em uma variavel)
lista_nome = "Breno", "Bruno", "Brenda", "Ana", "Amanda", "Antonela"
nome_1 = "Breno"
nome_2 = "Ana"

if nome_1 in lista_nome:
    print(f'{nome_1} está na lista')
else:
    print(f'{nome_1} não está na lista')

if nome_2 in lista_nome:
    print(f'{nome_2} está na lista')
else:
    print(f'{nome_2} não está na lista')