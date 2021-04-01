from abstractView import AbstractView

class EnfermeiroView(AbstractView):

    def tela_enfermeiro(self):
        print ("\n ---- Cadastro do Enfermeiro ----")
        print ("1 - Incluir Enfermeiro")
        print ("2 - Excluir Enfermeiro")
        print ("3 - Alterações no Cadastro")
        print ("4 - Listagem de Enfermeiros por matricula")
        print ("0 - Sair")
        opcao = self.le_inteiro('Digite uma opção: ')
        return opcao

    def incluir(self):
        nome_completo = input("Nome do Enfermeiro:")
        idade = input("Idade:")
        cpf = str(input("Digite o CPF:"))
        try:
            matricula_coren = input("Numero de matricula coren:")
        except ValueError as e:
            print('\nERRO: Digite um valor valido: {}'.format(e))
        else:
            self.clear()
            return [nome_completo, idade, cpf, matricula_coren]

    def excluir(self):
        try:
            matricula_coren = input("ID do vendedor:")
        except ValueError as e:
            print('\nERRO: Digite um valor valido: {}'.format(e))
        else:    
            return matricula_coren

    
    def listar(self, listagem):
        self.clear()
        print("\n Lista de Enfermeiros:")
        for enfermeiro in listagem:
            print("Nome: " + enfermeiro.nome_completo)
            print("Idade: "+ str(enfermeiro.idade))
            print("CPF: "+ enfermeiro.cpf)
            print("Matricula/COREN: " + enfermeiro.matricula_coren)

    def atualiza(self):
        nome_completo = input("Nome do Enfermeiro:")
        idade = input("Idade:")
        cpf = input("Digite o cpf:")
        try:
           matricula_coren = input("Digite a MATRICULA/COREN:")
        except ValueError as e:
            print('\nERRO: Digite um valor valido: {}'.format(e))
        else: 
            return [nome_completo, idade, cpf, matricula_coren]


    def selecionar(self, enfermeiros):
        count = 1
        print("Selecione um enfermeiro")
        for enfermeiro in enfermeiros:
            print("Paciente nº: ", count)
            print("Nome: " + enfermeiro.nome_completo)
            print("Idade: "+ str(enfermeiro.idade))
            print("Matricula: "+ str(enfermeiro.matricula))
            print("--------------------------------\n")

        escolha = self.le_inteiro("-->", range(1, count))
        return escolha


