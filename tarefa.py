class Tarefa:
    def __init__(self):
        self.__descricao = input('Descreva sua tarefa ')
        self.__status = input('Status da tarefa ')

    def criarTarefa(self):
        descricao = self.__descricao
        status = self.__status
        try:
            agenda = open('Agenda.txt', 'a')
            dados = f'{descricao} - {status} \n'
            agenda.write(dados)
            agenda.close()
            print(f'Tarefa salva com sucesso')
        except:
            print('Erro ao gravar tarefa!')

    def listarTarefa(self):
        agenda = open("agenda.txt", "r")
        for tarefa in agenda:
            print(tarefa)
        agenda.close()
