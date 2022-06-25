salarioINICIAL = 1000
aumento = 0
salario = 0
ano = 7
salarioFINAL = 0

print ("Em DOIS MIL E 5 o salario inicial desse funcionario era de R$: ", salarioINICIAL)
aumento = 1.5
print("O funcionario recebe o aumento de quantos %? ", aumento)

aumento = (aumento/100)+1
salario = aumento

print ("Em DOIS MIL E 6 o salário desse funcionario foi de R$: ", salario)
porcentagem = 3
print("\n Em DOIS MIL E 7 o funcionario teve aumento de quantos %? ", porcentagem)

salario = salario*((porcentagem/100)+1)

print ("O salario desse funcionario no ano de DOIS MIL E 7 foi de R$: ", salario)

for j in range(1,15):
    ano = ano+1
    porcentagem = porcentagem*2
    salario = salario*((porcentagem/100)+1)
    print("Em DOIS MIL E", ano, "o salario desse funcionario foi de R$: ", salario)

salarioFINAL = salario
print ("O salário atual desse funcionário é de R$: ", salarioFINAL)
