import random

print("#"*50)
print("             --- Online RPG Dice ---")
print("#"*50)
print("\n")

n_dados = int(input("Diga o numero de dados: "))
n_lados = int(input("Diga o numero de lados: "))
buff = int(input("Diga o valor do buff: "))
debuff = int(input("Diga o valor do debuff: "))
x = input("Deseja mostrar uma mensagem personalizada na saida(s/n)? ")
if x == "s":
    msg = input("Escreva sua mensagem: ")
elif x == "n":
    pass
else:
    print("Comando invalido, mensagem personalizada cancelada.")

print("\n")

for i in range(n_dados):
    sort = random.randint(1, n_lados)
    add_buff = sort + buff
    add_debuff = add_buff - debuff
    if x == "s":
        print(f"{msg}")
        print(f"Dado {i+1}: {add_debuff}")
        print(f"Valor do dado: {sort} // Buff: {buff} // Debuff: {debuff}\n")
    elif x == "n" or x != "s" and "n":
        print(f"Dado {i+1}: {add_debuff}")
        print(f"Valor do dado: {sort} // Buff: {buff} // Debuff: {debuff}\n")