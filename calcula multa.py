velocidadeAVENIDA = int (input("Digite a velocidade limite da avenida: "))
velocidadeCARRO = int (input ("Digite a velocidade que o motorista estava dirigindo: "))

velocidadeDIFERENCA = velocidadeCARRO-velocidadeAVENIDA

if velocidadeDIFERENCA>0 and velocidadeDIFERENCA<10:
    print ("A multa será de R$50,00")
elif velocidadeDIFERENCA>=11 and velocidadeDIFERENCA<=30:
    print ("A multa será de R$100,00")
elif velocidadeDIFERENCA>31:
    print ("A multa será de R$200,00")
else:
    print ("Dentro do limite de velocidade. Sem multas")
