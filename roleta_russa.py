import random
jogadores = []

msg1 = "foi o azarado da vez. Nao vai fazer falta."
msg2 = "foi o azarado da vez. O mundo agradece."
msg3 = "foi o azarado da vez. Jackpot!"
msg4 = "foi o azarado da vez. Ja vai tarde."

msg = [msg1, msg2, msg3, msg4]


print("#"*33)
print("--- Bem-vindo a Roleta Russa ---")
print("#"*33)
print("\n")


while True:
    player = input("Diga o nome do jogador e 'stop' para parar: ")
    if player != "stop":
        jogadores.append(player)
    else:
        break


print("\nAzarados de hoje:")
for player in jogadores:
    print(player)


print("\n<------- JOGO INICIADO ------->\n")

while True:
    if len(jogadores) > 1:
        morto = random.choice(jogadores)
        txt = random.choice(msg)
        print("A roleta esta girando...")
        print(f"{morto}", txt)
        print(f"Restam apenas {len(jogadores)} jogadores.")
        jogadores.remove(morto)
        print("-"*50)
    
    else:
        print(f"Parabens {jogadores[0]}, voce é o grande sortudo de hoje, mas quem sabe na proxima...\n")
        break