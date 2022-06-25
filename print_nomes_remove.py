resp = 'S'
respREMOVE = 'S'
nomes = []


 
     
while True:

    print("Digite um nome ou tecle 'S' para sair")
    resp = input()

    if(resp=='S') or (resp=='s'):
            break
        
    nomes.append(resp)
print("Lista: ", nomes)

        
print ("Deseja remover algum item da lista? ")
respREMOVE = input()
 
if(respREMOVE == 'S') or (respREMOVE=='s'):
    nomeREMOVE = input ("Qual nome você deseja remover? ")
    nomes.remove(nomeREMOVE)
print(nomes)
    

    
        


    
    
    
