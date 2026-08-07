# Existe uma forma de fazermos condições ao nosso codigo com if e else

#if     se
#else   se não

a = int(input("Digite um numero inteiro: "))
b = int(input("Digite o segundo numero inteiro: "))
c = a + b

if c > 100:
    print(f"O numero que você digitou primeiro {a} somado com {b} da mais do que 100")
else:
    print(f"O numero que você digitou primeiro {a} somado com {b} é menor ou igual a 100")