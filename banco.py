import random

class Banco:
    def __init__ (self, nome, nasc, cpf, saldo, dividas, universitario, aposentado):
        self.nome = nome
        self.nasc = nasc
        self.cpf = cpf
        self.saldo = saldo
        self.dividas = dividas
        self.universitario = universitario
        self.aposentado = aposentado

    def dados(self):
        print("\033[H\033[J", end="")
        print("\n--- INFORMAÇÕES DO CLIENTE ---\n")
        print(f"Nome: {self.nome}")
        print(f"Data de nascimento: {self.nasc}")
        print(f"CPF: {self.cpf}")
        print(f"Saldo: R$ {self.saldo}")
        print(f"Dividas ao banco: R$ {self.dividas}\n")
        x = input("Clique para voltar: ")
        if x == "a":
            print("\033[H\033[J", end="")
        else:
            pass

    def saque(self):
        print("\033[H\033[J", end="")
        print("\n--- REALIZAR SAQUE ---\n")
        print("Antes de prosseguirmos, prove sua identidade\n")
        password = int(input("Informe seu codigo de acesso: "))
        if password in senhas:
            print("\nIdentidade confirmada\n")
            saq = float(input("Informe o valor a ser retirado: "))

            if self.saldo >= saq:
                self.saldo -= saq
                print(f"\nSaque no valor de R$ {saq} reais feito!")
                print(f"Saldo disponivel: R$ {self.saldo}\n")
                x = input("Clique para voltar: ")
                if x == "a":
                    print("\033[H\033[J", end="")
                else:
                    pass

            elif saq > self.saldo:
                print("\nVoce não tem saldo o suficiente.")
                print(f"Saldo disponivel: R${self.saldo}\n")
                x = input("Clique para voltar: ")
                if x == "a":
                    print("\033[H\033[J", end="")
                else:
                    pass

        elif password not in senhas:
            print("\nCodigo invalido, a operacao foi cancelada.\n")
            x = input("Clique para voltar: ")
            if x == "a":
                print("\033[H\033[J", end="")
            else:
                pass

    def deposito(self):
        print("\033[H\033[J", end="")
        print("\n--- REALIZAR DEPOSITO ---")
        print("\nAntes de prosseguirmos, prove sua identidade\n")
        password = int(input("Informe seu codigo de acesso: "))
        if password in senhas:
            print("\nIdentidade confirmada\n")
            deposit = float(input("Diga o valor a ser depositado: "))
            
            if deposit >= 1:
                self.saldo += deposit
                print(f"\nDeposito de R${deposit} reais feito!")
                print(f"Saldo disponivel: R${self.saldo}\n")
                x = input("Clique para voltar: ")
                if x == "a":
                    print("\033[H\033[J", end="")
                else:
                    pass

            elif deposit <= 0:
                print(f"\nO valor minimo de deposito é R$ 1,00\n")

        elif password not in senhas:
            print("Codigo invalido, a operacao foi cancelada.")
            x = input("Clique para voltar: ")
            if x == "a":
                print("\033[H\033[J", end="")
            else:
                pass

    def alterar_dados(self):
        print("\033[H\033[J", end="")
        print("\n--- ALTERAR DADOS ---")
        print("1 - Mudar nome\n2 - Mudar data de nascimento\n3 - Mudar CPF\n4 - Mudar codigo de acesso")

        option = int(input("Escolha uma das opçoes acima: "))

        if option == 1:
            print(f"\nNome atual: {self.nome}")
            new_nome = input("Informe seu novo nome: ")
            self.nome = new_nome
            print("\nNome alterado com sucesso!")
            x = input("Clique para voltar: ")
            if x == "a":
                print("\033[H\033[J", end="")
            else:
                pass

        elif option == 2:
            print(f"\nData de nascimento atual: {self.nasc}")
            new_nasc = input("Informe a nova data com /: ")
            self.nasc = new_nasc
            print("\nData de nascimento alterada com sucesso!")
            x = input("Clique para voltar: ")
            if x == "a":
                print("\033[H\033[J", end="")
            else:
                pass

        elif option == 3:
            print(f"\nCPF atual: {self.cpf}")
            new_cpf = int(input("Informe seu novo CPF(somente os numeros): "))
            self.cpf = new_cpf
            print("\nCPF alterado com sucesso!")
            x = input("Clique para voltar: ")
            if x == "a":
                print("\033[H\033[J", end="")
            else:
                pass

        elif option == 4:
            print("\nPor medidas de segurança, prove que é voce")
            verificacao = int(input("Informe seu codigo de acesso: "))
            if verificacao in senhas:
                print("\nIdentidade confirmada!")
                new_codigo = int(input("Diga o novo codigo de acesso de 8 digitos: "))
                senhas.pop(0)
                senhas.append(int(new_codigo))
                print("\nCodigo de acesso alterado com sucesso!")
                x = input("Clique para voltar: ")
                if x == "a":
                    print("\033[H\033[J", end="")
                else:
                    pass
            elif verificacao not in senhas:
                print("\nCodigo invalido. Alteração negada.")
                x = input("Clique para voltar: ")
                if x == "a":
                    print("\033[H\033[J", end="")
                else:
                    pass

    def programas(self):
        
        print("\033[H\033[J", end="")
        print("--- BENEFICIOS DO BANCO ---\n")
        print("Veja a tabela a seguir com todos os beneficios e programas que o nosso banco fornece:\n")
        print("1 - Ajuda universitaria\n2 - Empestimo\n3 - Aposentadoria\n4 - Loteria\n5 - Meus programas\n6 - Fazer uma doacao\n7 - Sair")
        option = int(input("Informe um numero: "))

        if option == 1:
            print("\033[H\033[J", end="")
            print("--- PROGRAMA DE AJUDA UNIVERSITARIA ---\n")
            print("Esse programa tem como fim ajudar universitarios financeiramente, com o pagamento de um valor mensalmente mediante alguns criterios.")
            x = input("Voce tem interesse em participar desse programa(s/n)? ")

            if x == "s":
                print("\033[H\033[J", end="")
                print("--- AVALIACAO DE REQUESITOS NECESSARIOS ---\n")
                age = int(input("1 - Informe sua idade: "))
                facul = input("2 - Voce esta atualmente matriculado em alguma universidade(s/n)? ")
                debito = input("3 - Voce possui alguma divida com algum banco(s/n)? ")
                print("\n\nAnalisando candidato...\n\n")
                if age >= 18 and facul == "s" and debito == "n":
                    self.saldo += 500
                    self.universitario = True
                    print(f"Caro {self.nome}, após uma analise do seu perfil, concluimos que voce está de acordo com todos os criterios necessarios para fazer parte do PROGRAMA DE AJUDA UNIVERSITARIA. A primeira parcela do programa já foi paga a voce. Bons estudos!\n")
                    
                    x = input("Clique para voltar: ")
                    if x == "a":
                        print("\033[H\033[J", end="")
                    else:
                        pass
                else:
                    print(f"Caro {self.nome}, após uma analise do seu perfil, concluimos que voce nao cumpre todos os requisitos necessarios para fazer parte do programa. Por isso, sua solicitacao foi negada.")
                    x = input("Clique para voltar: ")
                    if x == "a":
                        print("\033[H\033[J", end="")
                    else:
                        pass

            elif x == "n":
                print("\nVoltando ao menu principal...\n")
                x = input("Clique para voltar: ")
                if x == "a":
                    print("\033[H\033[J", end="")
                else:
                    pass

        elif option == 2:
            print("\033[H\033[J", end="")
            print("--- SOLICITACAO DE EMPRESTIMO ---\n")
            print("Emprestimo é uma acao em que o cliente retira um valor do banco de forma emprestada, no qual o mesmo irá devolver a quantia retirada com uma taxa adicional, ou entao ficará em debito com o banco e nao podera ter acesso a diversos servicos.")
            x = input("Voce deseja solicitar um emprestimo com o nosso banco(s/n)? ")
            if x == "s":
                n1 = int(input("Diga o valor que deseja pedir em emprestimo: "))
                password = int(input("Por medidas de seguranca, informe seu codigo de acesso: "))
                if password in senhas:
                    n2 = n1 * 2.1
                    print("\n\n--- DETALHES DO EMPRESTIMO ---\n")
                    print(f"Valor solicitado: R$ {n1}\nDebito ao banco: R$ {n2}\n")
                    self.saldo += n1
                    self.dividas += n2
                    print("Emprestimo feito com sucesso!\nO valor já foi adicionado a sua conta, e a divida pode ser conferida no menu 'Informacoes'.\n")
                    y = input("Clique para voltar: ")
                    if x == "a":
                        print("\033[H\033[J", end="")
                    else:
                        pass   
                elif password not in senhas:
                    print("\nCodigo invalido, a operacao foi cancelada.\n")
                    y = input("Clique para voltar: ")
                    if x == "a":
                        print("\033[H\033[J", end="")
                    else:
                        pass

            elif x == "n":
                print("\nOperação cancelada...\n")
                y = input("Clique para voltar: ")
                if x == "a":
                    print("\033[H\033[J", end="")
                else:
                    pass

            else:
                print("\nComando invalido")

        elif option == 3:
            print("\033[H\033[J", end="")
            print("--- SOLICITACAO DE APOSENTADORIA ---\n")
            print("A aposentadoria é um programa voltado a pessoas idosas que já cumpriram os anos de trabalho exigidos de acordo com seu sexo, e podem contar com essa ajuda financeira para arcar com seus custos de vida basicos, mesmo sem um emprego formal.")
            x = input("Voce deseja fazer uma solicitacao de aposentadoria(s/n)? ")
            if x == "s":
                print("\n--- AVALIACAO DE REQUESITOS NECESSARIOS ---\n")
                print("Antes de prosseguirmos, responda esse questionario para sabermos se voce atende aos requesitos exigidos para o programa\n")

                idade = int(input("Quantos anos voce tem? "))
                contrib = int(input("Quantos anos de contribuicao voce tem? "))
                sexo = input("Qual o seu sexo(m/f)? ")

                if idade >= 65 and contrib >= 20 and sexo == "m":
                    self.saldo += 1500
                    self.aposentado = True
                    print("\nApós uma analise, nós pudemos observar que voce cumpre todos os requesitos necessarios para receber a sua aposentadoria. A primeira parcela já foi depositada em sua conta.\n")
                    
                    y = input("Clique para voltar: ")
                    if x == "a":
                        print("\033[H\033[J", end="")
                    else:
                        pass

                elif idade >= 62 and contrib >=15 and sexo == "f":
                    print("\nApós uma analise, nós pudemos observar que voce cumpre todos os requesitos necessarios para receber a sua aposentadoria. A primeira parcela já foi depositada em sua conta.\n")
                    self.saldo += 1500
                    aposentadoria = True
                    y = input("Clique para voltar: ")
                    if x == "a":
                        print("\033[H\033[J", end="")
                    else:
                        pass

                else:
                    print("\nApos uma analise criteriosa, pudemos notar que voce não cumpre com todos os requesitos necessarios para se aposentar, portanto sua solicitacao foi cancelada.\n")
                    y = input("Clique para voltar: ")
                    if x == "a":
                        print("\033[H\033[J", end="")
                    else:
                        pass

            elif x == "n":
                print("\nOperacao cancelada...\n")
                y = input("Clique para voltar: ")
                if x == "a":
                    print("\033[H\033[J", end="")
                else:
                    pass
            
        elif option == 4:
            print("\033[H\033[J", end="")
            print("--- BEM VINDO A LOTERIA ---\n")
            print("Compre uma ficha, aposte e concorra a R$300,00 reais depositados na hora! Aposte e caso os 3 numeros forem iguais, voce recebe na hora!")
            print("Cada ficha custa apenas R$2,00, e esse valor é tirado do seu saldo no banco.\n\n")
            n_fichas = int(input("Informe quantas fichas deseja comprar: "))

            valor_fichas = n_fichas * 2
            print("\033[H\033[J", end="")
            print("\n\n--- SORTEIO INICIADO ---\n\n\n")

            if self.saldo >= valor_fichas:

                for i in range(n_fichas):
                    n1 = random.randint(1, 10)
                    n2 = random.randint(1, 10)
                    n3 = random.randint(1, 10)
                    print("-"*30)
                    print("\n")
                    print(f"Sorteio N° {i+1}: | {n1} | {n2} | {n3} | ")
                    if n1 == n2 and n2 == n3:
                        print("Meus parabens!! Voce acabou de ganhar R$300,00!\n\n")
                        self.saldo += 300
                    else:
                        print("Não foi dessa vez...\n\n")

            elif self.saldo < valor_fichas:
                print("Saldo insuficiente!\n")

            self.saldo -= valor_fichas
            print("\nFim dos sorteios!\n")
            y = input("Clique para voltar: ")
            if y == "a":
                print("\033[H\033[J", end="")
            else:
                pass

        elif option == 5:
            print("\033[H\033[J", end="")
            print("--- SEUS PROGRAMAS ---\n")
            print("Confira aqui todos os programas em que voce participa:\n")

            if self.universitario == True:
                print("- Voce participa do programa de AJUDA UNIVERSITARIA.\n")
            if self.aposentado == True:
                print("- Voce participa do programa de APOSENTADORIA.\n")
            if self.universitario == False and self.aposentado == False:
                print("- Voce nao participa de nenhum programa.\n")

            y = input("Clique para voltar: ")
            if y == "a":
                print("\033[H\033[J", end="")
            else:
                pass

        elif option == 6:
            print("\033[H\033[J", end="")
            print("--- DOAÇÃO DE VALORES ---\n")
            print("Aqui é um espaco reservado para voce fazer uma doação para diversas instituições parceiras do nosso banco.\nAs instuições tem varios foco como ajuda a pessoas sem teto, pessoas em vulnerabilidade social, orfãos, entre diversos outros. Cada valor ajuda, e pode mudar a vida de uma pessoa.\n")

            x = input("Voce deseja fazer uma doacao comunitaria(s/n)? ")
            if x == "s":
                password = int(input("Por seguranca, informe seu codigo de aceso: "))
                if password in senhas:
                    print("\nIdentidade confirmada com sucesso\n\n")
                    doacao = int(input("Insira o valor a ser doado: "))
                    if self.saldo >= doacao:
                        self.saldo -= doacao
                        print("Sua doacao foi enviada com sucesso. Obrigado pela sua contribuicao!\n")
                        y = input("Clique para voltar: ")
                        if y == "a":
                            print("\033[H\033[J", end="")
                        else:
                            pass
                    elif doacao > self.saldo:
                        print("\nSaldo insuficiente para a doacao.\n")
                        y = input("Clique para voltar: ")
                        if y == "a":
                            print("\033[H\033[J", end="")
                        else:
                            pass

                elif password not in senhas:
                    print("\nCodigo invalido. Operacao cancelada\n")
                    y = input("Clique para voltar: ")
                    if y == "a":
                        print("\033[H\033[J", end="")
                    else:
                        pass

            elif x == "n":
                print("Operacao cancelada.")
                y = input("Clique para voltar: ")
                if y == "a":
                    print("\033[H\033[J", end="")
                else:
                    pass

    def quitar(self):
        print("\033[H\033[J", end="")
        print("--- QUITAR SUAS DIVIDAS ---\n")
        print("Aqui voce pode visualizar todas as suas dividas com o banco e paga-las\n")

        if self.dividas > 0:
            print(f"- Valor da sua divida: R${self.dividas}\n")

            x = input("Deseja quitar sua divida? OBS: O valor sera extraido do seu saldo nesse banco(s/n): ")
            if x == "s":
                if self.saldo > self.dividas:
                    password = int(input("Para prosseguir, informe seu codigo de acesso: "))
                    if password in senhas:
                        self.saldo -= self.dividas
                        self.dividas = 0
                        print("\n\nDivida quitada com sucesso!\n")

                        y = input("Clique para voltar: ")
                        if y == "a":
                            print("\033[H\033[J", end="")
                        else:
                            pass
                    elif password not in senhas:
                        print("\nCodigo invalido, a operacao foi cancelada.")

                elif self.dividas > self.saldo:
                    print("\nSaldo insuficiente!\n")
                    print(f"Divida: {self.dividas}\nSaldo: {self.saldo}\n")

                    y = input("Clique para voltar: ")
                    if y == "a":
                        print("\033[H\033[J", end="")
                    else:
                        pass
                
            elif x == "n":
                y = input("Clique para voltar: ")
                if y == "a":
                    print("\033[H\033[J", end="")
                else:
                    pass

        elif self.dividas <= 0:
            print("- Voce nao possui dividas com o banco.\n")
            y = input("Clique para voltar: ")
            if y == "a":
                print("\033[H\033[J", end="")
            else:
                pass

    def sair(self):
        print("\033[H\033[J", end="")
        print(f"Volte sempre, {self.nome}!")
        print("Fazendo Logout...")


senhas = []
nomes = []
acesso = False
adm = False

while True:

    print("\033[H\033[J", end="")
    print("--- Bem vindo, usuario! ---\n")
    print(f"1 - Fazer login\n2 - Criar conta\n3 - Encerrar")

    option = int(input("Informe um numero: "))

    if option == 1:
        print("\033[H\033[J", end="")
        print("--- FAZER LOGIN ---\n")
        verif_nome = input("Informe seu nome: ")
        if verif_nome in nomes:
            verif_codigo = int(input("Informe seu codigo de acesso: "))
            if verif_codigo in senhas:
                acesso = True
                break
            elif verif_codigo not in senhas:
                print("\nCodigo invalido")
                
        elif verif_nome not in nomes:
            print("\nNome nao cadastrado")
            x = input("Clique para voltar: ")
            if x == "a":
                print("\033[H\033[J", end="")
            else:
                pass

    elif option == 2:
        print("\033[H\033[J", end="")
        print("--- CRIAR CONTA ---\n")
        nome = input("Informe seu nome: ")
        nasc = input("Informe sua data de nascimento com /: ")
        cpf = int(input("Informe apenas os numeros do seu cpf: "))
        while True:
            senha = input("Informe um codigo de acesso de 8 digitos numericos: ")
            if len(senha) == 8 and senha.isdigit():
                break
            else:
                print("\nA senha precisa ter 8 digitos e totalmente numerica.\n")
        senha = int(senha)
        cliente = Banco(nome, nasc, cpf, 0, 0, False, False)
        senhas.append(senha)
        nomes.append(nome)
        print("\nConta criada com sucesso!")
        x = input("Clique para voltar: ")
        if x == "a":
            print("\033[H\033[J", end="")
           
            

    elif option == 3:
        print("\033[H\033[J", end="")
        print("Encerrando programa...")
        break

    elif option == 4:
        acesso = True
        adm = True
        cliente = Banco("Batata", "27/02/2008", 14129149490, 1000, 0, False, False)
        senhas.append(12345678)
        break
       

while acesso == True:
    print("\033[H\033[J", end="")
    if adm == False:
        print(f"--- Seja bem vindo, {nome} ---\n")
    elif adm == True:
        print("--- Seja bem vindo, Lorde Vittz ---\n")
    print("1 - Deposito\n2 - Saque\n3 - Informacoes\n4 - Alterar dados\n5 - Programas e beneficios\n6 - Quitar dividas\n7 - Sair")
    x = input("Informe um numero: ")

    if x == "1":
         cliente.deposito()

    elif x == "2":
        cliente.saque()
        
    elif x == "3":
        cliente.dados()

    elif x == "4":
        cliente.alterar_dados()

    elif x == "5":
        cliente.programas()

    elif x == "6":
        cliente.quitar()

    elif x == "7":
        if adm == False:
            print(f"\nVolte logo, {nome}.\n")
            break
        elif adm == True:
            print("\nAté logo, Lorde Vittz\n")
            break
    
    elif x == "":
        pass