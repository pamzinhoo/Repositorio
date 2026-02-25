palavra_secreta = "perfumaria"
tentativas = 0
letra_acertada = ''
letra_errada = ''

import os

while True:
    letra_digitada = input("Digite uma letra: ").lower()
    tentativas += 1
    if len(letra_digitada) > 1:
        print("Digite apenas uma letra")
        continue
    
    elif letra_digitada in palavra_secreta:
        letra_acertada += letra_digitada
        print("Você acertou uma letra")
    
    elif letra_digitada in letra_errada:
        print("Você ja digitou essa letra")
    else:
        print("Letra nova")
        letra_errada += letra_digitada
    
    
        
    palavra_formulada = ''
    for palavra_adivinha in palavra_secreta:
        if palavra_adivinha in letra_acertada:
            palavra_formulada += palavra_adivinha   
        else:
            palavra_formulada += "*"
    print(palavra_formulada)

    if palavra_formulada == palavra_secreta:
        os.system("cls") # Clear no terminal
        print("PARABENS!!")
        print(f"Você tentou {tentativas}x")
        break

