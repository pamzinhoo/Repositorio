""" 
Faça uma lista de compras com listas
O usuario deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
nao permita que o programa quebre com erros de indices inexistentes na lista
"""
import os
lista_compras = []
while True:
    opcao = input("[i]serir [a]pagar [l]ista\n").lower()
    # Digitar o item que quer adicionar a lista
    if opcao == "i":
        os.system("cls")
        inserir = input("Digite o valor: ")
        lista_compras.append(inserir)
        os.system("cls")
        continue
    
  
        
        
    elif opcao == "a":
        if len(lista_compras) == 0:
            print("Lista vazia")
        
        else:
            indice_deletar = input("Digite o indice que deseja apagar da sua lista: ")
            try:
                indice = int(indice_deletar)
                del lista_compras[indice]
            except:
                print("Digite um indice correto")
                continue
            
    # Ele printa a lista que tem coisas dentro
    elif opcao == "l":
        os.system("cls")
        if len(lista_compras) == 0:
            print("Lista vazia")
        for indice, nome in enumerate(lista_compras):
            print(indice, nome)
        continue
    else:
        print("Escolha uma das opções")
        continue
    

    
        
            

    




    
    

    
    
        
    