quantCOMODOS = int (input("Quantos comodos tem a casa? "))
areaTOTAL = 0

for j in range(quantCOMODOS):
    comodo = str (input("Qual comodo deseja calcular? "))
    largura = float (input("Digite a largura do cômodo: "))
    comprimento = float (input("Digite o comprimento do cômodo: "))
    area = largura*comprimento 
    print ("A áre do cômodo é: ", area)

    areaTOTAL = areaTOTAL+area

print ("A área da casa é: ", areaTOTAL)
