valorUM = int(input("Digite o primeiro valor: "))
valorDOIS = int (input("Digite o segundo valor: "))

if (valorUM>valorDOIS):
    print ("Erro!Operação iválida")

for x in range(valorUM, valorDOIS):
    b = x%2

    if (b==1):
        print ("Numero ímpar:", x)
        resultado=x+b
