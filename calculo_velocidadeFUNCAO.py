def velocidade_media (dist, temp):
    velo = divisao(dist, temp)
    return velo

def divisao (dist2, temp2):
    x = dist2/temp2
    return x

while True:
    distancia = float(input("Digite a distância (M): "))
    tempo = float(input("Digite o tempo (S): "))

    velocidade = velocidade_media(distancia,tempo)

    print (f"A velocidade média é {velocidade} m/s")
    resp = input("Deseja continuar [s] [n]")

    if(resp=='n'):
        break
