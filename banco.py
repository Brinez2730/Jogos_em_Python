class Banco:
    def __init__(self, cliente, nasc, cpf, saldo):
        self.cliente = cliente
        self.nasc = nasc
        self.cpf = cpf
        self.saldo = saldo

    def info(self):
        print("\nInformacoes do cliente:\n")
        print(f"Nome: {self.cliente}")
        print(f"Idade: {self.nasc} anos")
        print(f"CPF: {self.cpf}")
        print(f"Saldo: R$ {self.saldo}\n")

    def deposito(self):
        add = float(input("Diga o valor a ser depositado: "))
        self.saldo += add
        print("Deposito feito com sucesso!")
        print(f"Saldo: R$ {self.saldo}\n")

    def saque(self):
        remove = float(input("Diga o valor a ser sacado: "))
        self.saldo -= remove
        print("Saque feito com sucesso!")
        print(f"Saldo: R$ {self.saldo}\n")


senhas = []
tentativas = 3
acesso = False

print("\nBem vindo usuario! \n")

while True:

    print("1 - Fazer login\n2 - Criar conta")
    option = int(input("Informe um numero: "))

    if option == 1:
        print("\n")
        print("--- Login do usuario ---\n")
        login = int(input("Informe seu codigo de acesso: "))

        if login in senhas:
            print("Login feito com sucesso!")
            acesso = True
            break
        elif len(senhas) == 0:
            print("\nNão há contas cadastradas.\n")
        elif login not in senhas:
            tentativas -= 1
            print(f"\nCodigo de acesso invalido. {tentativas} tentativas restantes.\n")
        elif tentativas <= 0:
            print("Tentativas esgotadas. O sistema sera encerrado.")
            break

    elif option == 2:
        print("\n")
        print("--- Criacao de conta ---\n")

        nome = input("Informe seu nome: ")
        nasc = input("Diga sua data de nascimento com /: ")
        cpf = int(input("Informe somente os numeros do seu CPF: "))
        criar_senha = input("Informe um codigo de acesso de 8 digitos: ")
        if len(criar_senha) < 8 or len(criar_senha) > 8:
            print("A senha precisa ter 8 digitos.\n")
        elif len(criar_senha) == 8:
            senhas.append(int(criar_senha))
            print("Conta criada com sucesso!\n")
            cliente = Banco(nome, nasc, cpf, 0)

    else:
        print("Opcao invalida.\n")

while acesso == True:
    print(f"Bem vindo, {nome}.\n")
    print("1 - Deposito\n2 - Saque\n3 - Informacoes\n4 - Sair")
    x = int(input("Informe um numero: "))

    if x == 1:
         cliente.deposito()

    elif x == 2:
        cliente.saque()
        
    elif x == 3:
        cliente.info()

    elif x == 4:
        print(f"Volte logo, {nome}.\n")
        break

    else:
        print("Codigo invalido.\n")