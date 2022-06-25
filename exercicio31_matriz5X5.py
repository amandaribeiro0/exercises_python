numero = 0
x = 0
linhaUM = [0,0,0,0,0]
linhaDOIS = [0,0,0,0,0]
linhaTRES = [0,0,0,0,0]
linhaQUATRO =[0,0,0,0,0]
linhaCINCO =[0,0,0,0,0]
somaNUMEROS = 0
somaCOLUNA = 0
somaLINHA = 0
somaPRINCIPAL = 0
somaSECUNDARIA = 0


sala = [linhaUM,linhaDOIS,linhaTRES,linhaQUATRO,linhaCINCO]
for linha in sala:
    for x in range (0,5):
        numero = int(input("Digite um numero: "))
        #linha.append(numero)
        somaNUMEROS = somaNUMEROS + numero
        if (x==2):
            somaCOLUNA = somaCOLUNA+numero
for linha in sala:
    somaPRINCIPAL = somaPRINCIPAL + linha[x]
    x = x+1
    somaSECUNDARIA=somaSECUNDARIA+linha[(len(linha)-x)]
'''
for x in range (0,5):
    linhaDOIS[x] = input(numero)
    
for x in range (0,5):
    linhaTRES[x] = input(numero)
    
for x in range (0,5):
    linhaQUATRO[x] = input(numero)
    
for x in range (0,5):
    linhaCINCO[x] = input(numero)
'''
print (linhaUM)
print (linhaDOIS)
print (linhaTRES)
print (linhaQUATRO)
print (linhaCINCO)
print (sala)
print ("A soma de todos os numeros é: ", somaNUMEROS)
print (f "A soma dos numeros da terceira linha: {sum(somaLINHA)}")
print ("A soma dos numeros da segunda coluna: ", somaCOLUNA)
print ("A soma da diagonal principal é: ", somaPRINCIPAL)
print ("A soma da diagonal secundaria é: ", somaSECUNDARIA)
