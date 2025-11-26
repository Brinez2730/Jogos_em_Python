import random

hp = 10
mana = 6
hp_ladrao = 5
noite = True
morte = False
ataque = False
check = False


while True:
    
    print("\nA noite vai chegando e voce ve um bom lugar para acampar, o que voce vai fazer?\n")
    x = random.randint(1,2)
    if x == 1:
        ataque = True
    elif x == 2:
        ataque = False

    while noite == True:
        print("1 - Dormir\n2 - Olhar os arredores\n3 - Continuar")
        acao = input("O que voce vai fazer? ")

        if acao == "1":
            if ataque == False:
                print("Voce teve uma boa noite de sono, e se sente revigorado para continuar a jornada.")
                print("mana e hp recuperados.\n")
                mana = 6
                hp = 10
                noite = False

            elif ataque == True:
                verificar = input("Enquanto voce dormia, voce acorda pensando ter ouvido algum barulho,\nvoce vai verificar(s/n)?")
                if verificar == "n":
                    print("Ladrões apareceram durante seu sono e te mataram. Pobre homem...")
                    morte = True
                    break

                elif verificar == "s":
                    print("\nVoce acordou e encontrou um ladrao escondido, agora é matar ou morrer. O que vai fazer?")
                    while hp_ladrao > 0:
                        acao = input("1 - Atacar\n2 - Se defender\n3 - Correr\n4 - Usar magia\nDiga a opção: ")

                        if acao == "1":
                            x = random.randint(1,2)
                            if x == 1:
                                print(f"O ladrao esquivou e contra atacou.\n")
                                hp -= 1
                                print(f"Seu HP: {hp} // HP do ladrao: {hp_ladrao} // Mana: {mana}")
                                print("-"*50,"\n")
                            elif x == 2:
                                print(f"Voce conseguiu bater no ladrao, mas ele ainda esta de pé.\n")
                                y = random.randint(1, 10)
                                if y != 10:
                                    hp_ladrao -= 1
                                elif y == 10:
                                    print("Parabens, voce deu um dano critico!\n")
                                    hp_ladrao -= 2
                                print(f"Seu HP: {hp} // HP do ladrao: {hp_ladrao} // Mana: {mana}")
                                print("-"*50,"\n")

                        elif acao == "2":
                            x = random.randint(1,2)
                            if x == 1:
                                print(f"O ladrao percebeu e não atacou.\n")
                                print("-"*50,"\n")
                            elif x == 2:
                                print(f"O ladrao atacou e voce se defendeu.\n")
                                print("-"*50,"\n")

                        elif acao == "3":
                            x = random.randint(1, 3)
                            if x == 1:
                                print(f"O ladrao te alcançou e te deu uma voadora.\n")
                                print("-5 de HP\n")
                                hp -= 5
                                print(f"Seu HP: {hp} // HP do ladrao: {hp_ladrao} // Mana: {mana}")
                                print("-"*50,"\n")
                            elif x == 2:
                                print("Voce conseguiu fugir da briga, sem honra mas com vida.\n")
                                fuga = True
                                break
                            elif x == 3:
                                print(f"O ladrao percebeu a sua covardia e te deu um golpe fatal na cabeca.\n")
                                hp -= 11
                                fuga = True
                                break
                            
                        elif acao == "4":
                            x = random.randint(1,2)
                            if x == 1:
                                print("Voce errou o alvo, e usou mana atoa.\n")
                                mana -= 2
                                print(f"Seu HP: {hp} // HP do ladrao: {hp_ladrao} // Mana: {mana}")
                                print("-"*50,"\n")
                            elif x == 2:
                                if mana > 0:
                                    print(f"Voce acertou o ladrao, mas ele ainda esta de pé.\n")
                                    mana -= 2
                                    hp_ladrao -= 2
                                    print(f"Seu HP: {hp} // HP do ladrao: {hp_ladrao} // Mana: {mana}")
                                    print("-"*50,"\n")
                                elif mana <= 0:
                                    print("Voce não tem mana o suficiente.\n")

                        

                        if hp_ladrao <= 0:
                            print("Voce venceu a luta e conseguiu dormir, e de manha se sentiu revigorado.\n")
                            print("mana e hp recuperados\n")
                            hp = 10
                            mana = 6
                            break
                        if hp <= 0:
                            print("Voce nao conseguiu vencer a luta, mas pelo menos agora pode descansar em paz.\n")
                            morte = True
                            break


                    if (hp_ladrao <= 0) or (hp <= 0):
                        break

        elif acao == "2":
            if check == False:
                if ataque == True:
                    print("Voce encontrou um ladrao por perto e conseguiu derrotar ele. Agora o ambiente está seguro.\n")
                    ataque = False
                    check = True
                
                elif ataque == False:
                    print("Voce nao viu nada demais por perto, o lugar é seguro.\n")
                    check = True

            elif check == True:
                print("Voce já verificou os arredores, não é mais necessario.\n")

        elif acao == "3":
            print("A exaustao tomou conta de voce, e voce acabou desmaiando no meio do caminho.")
            print("-5 de hp\n")
            hp -= 5
            noite = False

        else:
            print("Acao invalida.\n")


    if (hp_ladrao <= 0) or (hp <= 0):
        break

    if noite == False: 
        break

    if morte == True:
        break