base = int (input("Digite o número da base: "))
expo = int (input("Digite o número expoente: "))
pot = 1

for j in range (expo):
    pot = base*pot

print (pot)
