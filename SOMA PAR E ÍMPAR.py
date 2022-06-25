somaPAR = 0
somaIMPAR = 0

for j in range (1,11):
    numero = int(input ("Digite um número"))
    b = numero%2
    if (b==0):
        somaPAR = int (somaPAR+numero)

    if (b==1):
        somaIMPAR = int (somaIMPAR+numero)

print ("A soma dos números pares é: ", somaPAR)
print ("A soma dos números ímpares é: ", somaIMPAR)
    
