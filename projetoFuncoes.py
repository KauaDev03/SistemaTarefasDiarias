tarefas_diarias = []

def adicionar_tarefa(nome, descricao, prioridade, categoria, status='andamento'):
    tarefa = {
        'Nome':nome,
        'Descrição':descricao,
        'Prioridade':prioridade,
        'categoria':categoria,
        'status':status
    }
    tarefas_diarias.append(tarefa)
    print('Tarefa adicionada com sucesso!')


def listar_todas_as_tarefas():
    if not tarefas_diarias:
        print('Você não possui nenhuma tarefa adicionada!')
    else:
        print('Listas de tarefas:\n ')

        for t in tarefas_diarias:
            for c, v in t.items():
                print(f'{c} = {v}')
            print('='*20)
            print()


def marcar_tarefa_concluida(tarefa):
    for t in tarefas_diarias:
        if t['Nome'] == tarefa:
            t['status'] = 'Concluido'


def filtrar_tarefas():
    menu = '''
    [1] categoria
    [2] ordem de prioridade
    [3] concluidas
    [4] aguardando
    '''
    while True:
        print('Você quer filtrar por: ')
        print(menu)
        escolha = str(input('Digite uma opção: '))

        if escolha == '1':
            escolha_categoria = input('Escolha a categoria que você quer filtrar: ').lower()
            encontrado = False
            for t in tarefas_diarias:
                if t['categoria'] == escolha_categoria:
                    for c, v in t.items():
                        print(f'{c} = {v}')
                    print('='*20)
                    encontrado = True          

            if not encontrado:
                print('Nenhuma tarefa encontrada para essa categoria.')
            else:
                break

        elif escolha == '2':
            tarefas_ordenadas = sorted(tarefas_diarias, key=lambda x: x['Prioridade'])
            for t in tarefas_ordenadas:
                for c, v in t.items():
                    print(f'{c} = {v}')
                print('='*20)
                print()
            break
                    
        elif escolha == '3':
            concluido=False
            for t in tarefas_diarias:
                if t['status'] == 'Concluido':
                    for c, v in t.items():
                        print(f'{c} = {v}')
                    print('='*20)
                    concluido = True
            if not concluido:
                print('Não existem tarfas concluidas')
            else:
                break
        
        elif escolha == '4':
            andamento=False
            for t in tarefas_diarias:
                if t['status'] == 'andamento':
                    for c, v in t.items():
                        print(f'{c} = {v}')
                    print('='*20)
                    andamento = True
            if not andamento:
                print('Não existem tarfas em andamento')
            else:
                break
        
        else:
            print('Opção Invalida!')



menu = '''
[1] - ADICIONAR TAREFA
[2] - LISTAR TODAS AS TAREFAS
[3] - MARCAR TAREFA COMO CONCLUIDA
[4] - FILTRAR TAREFAS
[5] - SAIR
'''

while True:
    print(menu)
    opcao = str(input('Escolha uma opção: '))
    if opcao == '1':
        nome = str(input('Digite o nome da tarefa: ')).lower()
        descricao = str(input('Digite uma descrição: ')).lower()
        prioridade = int(input('Qual a prioridade: '))
        categoria = str(input('Digite a categoria da tarefa: ')).lower()
        adicionar_tarefa(nome, descricao, prioridade, categoria)
        
    elif opcao == '2':
        listar_todas_as_tarefas()

    elif opcao == '3':
        nome_tarefa = str(input('Qual tarefa deseja marcar como concluida? ')).lower()
        marcar_tarefa_concluida(nome_tarefa)

    elif opcao == '4':
        filtrar_tarefas()

    elif opcao == '5':
        break
    
    else:
        print('opção inválida!')
