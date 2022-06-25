resp = "S"

while (resp=="S"):
    meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']
    try:
        index = int(input("Digite um número para apresentar um mês: "))
        print(meses[index-1])
    except:
        print ("Dados iválidos")
        
    resp = input ("Deseja continuar? [S/N] ")
    if (resp=="N"):
        print ("Programa finalizado.")
