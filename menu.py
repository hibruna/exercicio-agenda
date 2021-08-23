from contato import Contato
from tarefa import Tarefa

def Menu():
    contato = Contato()
    tarefa = Tarefa()
    opcao = input('[1]Para cadastrar contato, [2] Para listar contato, [3] Para excluir contato,'
                  '[4] Para criar tarefas, [5] Para listar tarefas.  '
                  'Opção desejada = ')
    if opcao == '1':
        contato.cadastrarContato()

    elif opcao == '2':
        contato.listarContato()

    elif opcao == '3':
        contato.excluirContato()

    elif opcao == '4':
        tarefa.criarTarefa()

    elif opcao == '5':
        tarefa.listarTarefa()

    else:
        print('Opção inválida')

Menu()
