x = 0

def soma(n1, n2):
    soma = n1+n2
    print(f"A soma é igual: {soma}")

def subtracao (a1, a2):
    subtracao = a1-a2
    print (f"A subtração é igual: {subtracao}")

def multiplicacao (x1, x2):
    multiplicacao = x1*x2
    print (f"A multiplicação é igual: {multiplicacao}")

def divisao (y1, y2):
    divisao = y1/y2
    print (f"A divisão é igual: {divisao}")


while x < 1:
    numeroUM = int(input("Digite um número: "))
    numeroDOIS = int(input("Digite um número: "))
    
    soma (numeroUM, numeroDOIS)
    subtracao(numeroUM, numeroDOIS)
    multiplicacao (numeroUM, numeroDOIS)
    divisao (numeroUM, numeroDOIS)
    
    
    x = x+1
   
