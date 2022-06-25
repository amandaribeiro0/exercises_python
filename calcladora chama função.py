x = 0

def soma(n1, n2):
    som = n1+n2
    return som

def subtracao (a1, a2):
    sub = a1-a2
    return sub

def multiplicacao (x1, x2):
    multip = 0
    for x in range(x2):
        multip = soma(x1,multip)
        print (multip)
    return multip

def divisao (y1, y2):
    div = y1/y2
    return div


while True:
    numeroUM = int(input("Digite um número: X1 "))
    numeroDOIS = int(input("Digite um número: X2 "))
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
