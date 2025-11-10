print("#"*50)
print("           --- Online Calculator ---")
print("#"*50)
print("\n")

print("<- Tabela de operaçoes ->")
print("+ = Soma")
print("- = Subtração")
print("* = Multiplicação")
print("/ = Divisão\n")

n1 = int(input("Diga o primeiro numero: "))
n2 = int(input("Diga o segundo numero: "))
op = input("Diga a operação: ")
print("\n")

if op == "+":
    out = n1 + n2
    print(f"A soma deu {out}.\n")

elif op == "-":
    out = n1 - n2
    print(f"A subtração deu {out}.\n")

elif (op == "*") or (op == "x"):
    out = n1 * n2
    print(f"A multiplicação deu {out}.\n")

elif op == "/":
    out = n1 / n2
    print(f"A divisão deu {out}.\n")

else:
    print("Operação invalida, programa encerrado.\n")