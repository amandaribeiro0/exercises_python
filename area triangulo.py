area = 0
resp = "S"

while (resp == "S"):
    base = float (input("Digite a base do triângulo: "))
    altura = float (input("Digite a altura do triângulo: "))
    if (altura+altura<base):
        print ("Erros!! Dados inválidos.")
    else:
        area = (base*altura)/2
        print ("A área do triângulo é: ", area)

    resp = str (input("Deseja efetuar novamente a operação? [S/N]"))

    if (resp == "N"):
        print ("Operação encerrada.")
