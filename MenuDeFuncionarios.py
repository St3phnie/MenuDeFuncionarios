print('Bem-vindo à empresa da Stephanie Marrocos')
print('-----------------------------------------')
print('------------MENU PRINCIPAL---------------')

# Lista de funcionários e variável ID global
listaFuncionarios = []
idGlobal = 4882986

# Função para cadastrar funcionário
def cadastrar_funcionario(id):
    print('-----------------------------------------')
    print('-------MENU CADASTRAR FUNCIONÁRIO--------')
    nome = input('Informe o nome do funcionário: ')
    setor = input('Informe o setor: ')
    salario = input('Informe o salário: ')

    funcionario = {
        'id': id,
        'nome': nome,
        'setor': setor,
        'salario': salario
    }

    listaFuncionarios.append(funcionario.copy())
    print(f'Funcionário cadastrado com sucesso!\nID: {id}')
    print(f'Nome: {nome}')
    print(f'Setor: {setor}')
    print(f'Salário: {salario}')
    print('----------------------')

# Função para consultar funcionários
def consultar_funcionarios():
    print('----------------------------------------')
    print('-------MENU CONSULTAR FUNCIONÁRIO-------')
    while True:
        print('\nEscolha a opção desejada:')
        print('1 - Consultar Todos')
        print('2 - Consultar por ID')
        print('3 - Consultar por Setor')
        print('4 - Retornar ao Menu')
        opcao = input('Escolha a opção desejada: ')
        if opcao == "1":
            if listaFuncionarios:
                for func in listaFuncionarios:
                    print(f'\nID: {func["id"]}')
                    print(f'Nome: {func["nome"]}')
                    print(f'Setor: {func["setor"]}')
                    print(f'Salário: {func["salario"]}')
                    print('----------------------')
            else:
                print('Nenhum funcionário cadastrado.')
        elif opcao == '2':
            idConsulta = int(input('Digite o ID do funcionário: '))
            encontrado = False
            for func in listaFuncionarios:
                if func['id'] == idConsulta:
                    print(f'\nID: {func["id"]}')
                    print(f'Nome: {func["nome"]}')
                    print(f'Setor: {func["setor"]}')
                    print(f'Salário: {func["salario"]}')
                    print('----------------------')
                    encontrado = True
                    break
            if not encontrado:
                print('Funcionário não foi localizado.')
        elif opcao == '3':
            setorConsulta = input('Digite o setor do funcionário: ')
            encontrado = False
            for func in listaFuncionarios:
                if func['setor'].lower() == setorConsulta.lower():
                    print(f'\nID: {func["id"]}')
                    print(f'Nome: {func["nome"]}')
                    print(f'Setor: {func["setor"]}')
                    print(f'Salário: {func["salario"]}')
                    print('----------------------')
                    encontrado = True
            if not encontrado:
                print('Nenhum funcionário foi localizado nesse setor.')
        elif opcao == '4':
            return
        else:
            print('Opção Inválida.')

# Função para remover funcionário
def remover_funcionario():
    while True:
        idRemocao = int(input('Digite o ID do funcionário que deseja remover: '))
        encontrado = False
        for func in listaFuncionarios:
            if func['id'] == idRemocao:
                listaFuncionarios.remove(func)
                encontrado = True
                print('Funcionário removido com sucesso')
                return
        if not encontrado:
            print('ID inválido.')

# Estrutura de menu do código principal (main)
while True:
    print('\nEscolha a opção desejada:')
    print('1 - Cadastrar Funcionário')
    print('2 - Consultar Funcionário')
    print('3 - Remover Funcionário')
    print('4 - Encerrar Programa')
    opcao = input('Escolha a opção desejada: ')
    if opcao == '1':
        idGlobal += 1
        cadastrar_funcionario(idGlobal)
    elif opcao == '2':
        consultar_funcionarios()
    elif opcao == '3':
        remover_funcionario()
    elif opcao == '4':
        print('Programa encerrado!')
        break
    else:
        print('Opção inválida.')
