ladoA = int (input ("Digite o primeiro lado do triângulo: "))
ladoB = int (input ("Digite o segundo lado do triângulo: "))
ladoC = int (input ("Digite o terceiro lado do triângulo: "))

if ladoA==ladoB and ladoB==ladoC:
    print ("Equilatero")
elif ladoA==ladoB or ladoA==ladoC or ladoB==ladoC:
    print ("Isoceles")
else:
    print ("Escaleno")
