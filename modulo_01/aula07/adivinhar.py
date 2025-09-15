num_secr = 23
for i in range(5):
    tentativa = int(input("Digite seu palpite: "))
    if int(tentativa) < num_secr:
        print("Muito baixo")
    elif tentativa > num_secr:
        print("Muito alto")
    else:
        tentativa == num_secr
        print("Parabens voce acertou")
        break
           
    if i == 4:
        print(f"Game Over, o numero era: {num_secr}")