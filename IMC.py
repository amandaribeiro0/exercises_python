peso =float (input("Digite seu peso: "))
altura = float (input("Digite sua altura: "))

imc = peso/(altura*altura)

#Classificação seguindo a tabela de IMC

if (imc<18):
    print("Magreza")
elif (imc>18) and (imc<25):
    print ("Saudável")
elif (imc>=25) and (imc<30):
    print ("Sobrepeso")
elif (imc>=30):
    print ("Obesidade")
    
