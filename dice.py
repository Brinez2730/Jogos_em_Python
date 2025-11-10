import random

print("#"*50)
print("               --- Online Dice ---")
print("#"*50)
print("\n")

n = int(input("Diga o numero de lados: "))

x = random.randint(1, n)
print(f"\nO seu dado de {n} lados rolou e um {x} surgiu.")