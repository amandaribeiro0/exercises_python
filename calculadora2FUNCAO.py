x = 0

def soma(n1, n2):
    soma = n1+n2
    return soma

def subtracao (a1, a2):
    subtracao = a1-a2
    return subtracao

def multiplicacao (x1, x2):
    multiplicacao = x1*x2
    return multiplicacao

def divisao (y1, y2):
    divisao = y1/y2
    return divisao


while True:
    numeroUM = int(input("Digite um número: "))
    numeroDOIS = int(input("Digite um número: "))
    operacao = input ("Qual operaçao deseja realizar?  [+] [-] [X] [:]")
    
    if (operacao=='+'):
        result = soma(numeroUM, numeroDOIS)
    elif (operacao=='-'):
        result = subtracao(numeroUM, numeroDOIS)
    elif (operacao=='x') or (operacao=='X'):
        result = multiplicacao(numeroUM, numeroDOIS)
    elif (operacao==':'):
        result = divisao(numeroUM, numeroDOIS)

    print ("O resultado é: ", result) 
    resp = input ("Deseja continuar? [S] [N]")

    if (resp=='n') or (resp=='N'):
        break
   
