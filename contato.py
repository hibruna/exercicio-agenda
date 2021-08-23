class Contato:
    def __init__(self):
        self.__nome = input('Nome do contato ')
        self.__email = input('Email para contato ')
        self.__telefone = input('Telefone para contato ')

    def cadastrarContato(self):
        try:
            agenda = open('Agenda.txt', 'a')
            dados = f'{__nome}; {__email}; {__telefone} \n'
            agenda.write(dados)
            agenda.close()
            print('Contato salvo com sucesso')
        except:
            print('Erro na gravação do contato')

    def listarContato(self):
        agenda = open("agenda.txt", "r")
        for contato in agenda:
            print(contato)
        agenda.close()

    def excluirContato(self):
        nomeDeletado = input('Digite o nome do contato que você deseja excluir ')
        agenda = open("agenda.txt", "r")
        aux = []
        aux2 = []
        for i in agenda:
            aux.append(i)
        for i in range(0, len(aux)):
            if nomeDeletado not in aux[i]:
                aux2.append(aux[i])
        agenda = open('agenda.txt', 'w')
        for i in aux2:
            agenda.write(i)
        print('Contato excluído com sucesso!')
        self.listarContato()
