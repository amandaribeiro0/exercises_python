soma = 0
divisao = 0
subtracao = 0
multiplicacao = 0
resp = "s"

while (resp == "s"):
    numeroUM = float(input("Digite um número: "))
    numeroDOIS = float(input ("Digite outro número: "))

    if (numeroUM==30000) or (numeroDOIS==30000):
        print("Programa finalizado")
    else:
        soma = numeroUM+numeroDOIS
        print ("A soma dos números é: ", soma)
        subtracao = numeroUM-numeroDOIS
        print ("o resultado da subtração é: ", subtracao)
        multiplicacao = numeroUM*numeroDOIS
        print ("O resultado da multiplicação é de: ", multiplicacao)
        divisao = numeroUM/numeroDOIS
        print ("O resultado da divisão é: ", divisao)

        
    resp = str (input("Deseja continuar a execução do programa? [s/n] "))
    if (resp=="n"):
        print ("Programa finalizado")




