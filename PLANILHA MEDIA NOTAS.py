reprovados = 0
aprovados = 0
exames = 0
mediaC = 0

for j in range(1,7):
    nome = str(input("Digite o nome do aluno: "))
    notaUM = float(input("Digite a primeira nota: "))
    notaDOIS = float(input("Digite a segunda nota: "))
    media = (notaUM+notaDOIS)/2
    print ("A media das notas é: ", media)

    if (media<=3):
        print ("Reprovado")
        reprovados = reprovados+1
    elif (media>3) and (media<=7):
        print ("Exame")
        exames = exames+1
    else:
        print ("Aprovado")
        aprovados = aprovados+1

    

    mediaC = (media+mediaC)
mediaC = mediaC/6
print ("A media da classe é:", mediaC)
print ("O total de aprovados é:", aprovados)
print ("O total de reprovados é:", reprovados)
print ("O total de alunos de recuperação é:", exames)
