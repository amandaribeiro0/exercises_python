a = 0
b = 1
x = 0

print("Sequência de Fibonacci\n")
num = int(input("Digite o número que vai começar essa sequência: "))
posicao = int(input("Digite a posição desejada: "))

for i in range(1,31):
    x = a+b
    a = b
    b = x

    if(posicao == i):
        print("\nO número que representa essa posição é: ", x)