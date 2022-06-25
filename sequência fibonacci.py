x = 0

num = int(input("Digite o numero para começar a seqência: "))

for j in range(1,31):
    x = x+num
    num = x-num
    print(x)
