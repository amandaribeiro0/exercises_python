salarioANTIGO = float (input("Digite seu salario atual: "))
#Aumento salarial

if salarioANTIGO < 1000:
    salarioATUAL = salarioANTIGO*1.25
    print ("Seu novo salario é: ", salarioATUAL)
elif salarioANTIGO >=1000 and salarioANTIGO < 2000:
    salarioATUAL = salarioANTIGO*1.15
    print ("Seu novo salario é: ", salarioATUAL)
elif salarioANTIGO >=2000:
    salarioATUAL = salarioANTIGO*1.10
    print ("Seu novo salario é: ", salarioATUAL)
    
