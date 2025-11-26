import random

hp = 10
fome = 10
bixos = ["coelho", "galinha", "rato", "lobo", "peixe"]
fuga = False

while True:

    print("\nDurante sua caminhada, voce sente fome e ve um arbusto com algumas\nfrutas nele que voce nunca viu na sua vida, o que vai fazer?\n")

    while fome > 0:
        print("1 - Caçar algo\n2 - Comer a fruta\n3 - Ignorar\n4 - Rezar")
        acao = input("O que voce vai fazer? ")

        if acao == "1":
            comida = random.choice(bixos)
            if comida == "coelho":
                print("Voce conseguiu capturar um coelho. Nao ajudou muito, mas é melhor que nada.\n")
                print("-3 de fome\n")
                fome -= 3
                print(f"Fome: {fome}")

            elif comida == "galinha":
                print("Voce conseguiu capturar uma galinha. Ajudou bastante, mas nao foi o suficiente.\n")
                print("-5 de fome\n")
                fome -= 5
                print(f"Fome: {fome}")

            elif comida == "rato":
                sorte = random.randint(1, 3)
                if sorte == 1 or sorte == 2:
                    print("Voce conseguiu capturar um rato. Alem de nao ajudar em nada na fome, voce se intoxicou e acabou morrendo.\n")
                    fuga = True
                    break
                
                elif sorte == 3:
                    print("Voce conseguiu capturar um rato. Nao ajudou muito, mas é melhor que nada.\n")
                    print("-1 de fome\n")
                    fome -= 1
                    print(f"Fome: {fome}")

            elif comida == "lobo":
                print("Voce com muito esforco e alguns arranhoes conseguiu capturar um lobo. Foi mais que o suficiente, e voce ja se sente pronto para continuar a jornada.\n")
                print("fome zerada\n-2 de hp\n")
                fome -= 10
                hp -= 2
                print(f"Fome: 0 // HP: {hp}")
                break

            elif comida == "peixe":
                print("Voce conseguiu pescar um bom peixe. Quase foi o suficiente, mas ja ajudou bastante.\n")
                print("-7 de fome")
                fome -= 7
                print(f"Fome: {fome}")

        elif acao == "2":
             comer = input("Voce analisa as frutas e nao tem certeza se elas sao comestiveis, voce realmente vai comer(s/n)? ")
             if comer == "s":
                sorte = random.randint(1, 2)
                if sorte == 1:
                    print("As frutas eram comestiveis e deliciosas, e voce ja se sente pronto para continuar sua jornada.\n")
                    print("fome zerada\n")
                    fome -= 10
                    break

                elif sorte == 2:
                    print("As frutas realmente eram venenosas, e voce sucumbiu rapido.\n")
                    fuga = True
                    break

             elif comer == "n":
                print("Voce nao se sentiu seguro em comer elas, e continua com fome.\n")

        elif acao == "3":
            print("Voce decide continuar a jornada mesmo com fome. Nao foi facil, mas voce conseguiu.\n")
            print("+2 de fome\n-3 de hp\n")
            fome += 2
            hp -= 3
            print(f"Fome: {fome} // HP: {hp}")
            fuga = True
            break

        elif acao == "4":
            bencao = random.randint(1, 10)
            if bencao != 10:
                print("Voce rezou por comida e...\nNão funcionou, que pena.\n")

            elif bencao == 10:
                print("Voce rezou por comida e...\nMilagrosamente, um grande cervo apareceu na sua frente. Voce saciou a sua fome e continuou sua jornada.\n")
                print("fome zerada\n+999 de fé\n")
                fome -= 10
                break

        else:
            print("Comando invalido.\n")

        if fome <= 0:
            print("Voce conseguiu se saciar e agora pode continuar a jornada!\n")
            fuga = True
            break

    if fome <= 0:
        break

    if fuga == True:
        break