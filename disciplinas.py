from codigo_matricula import gerar_codigo_matricula
from professores import listar_professores, professores

def cadastrar_disc():
    print('Olá, este é o cadastro de disciplinas, vamos começar!')
    nome = input('Digite o nome da disciplina: \n')
    codigo = gerar_codigo_matricula()
    carga = int(input('Digite a carga horária da disciplina: \n'))
    
    if professores:
        print('Professores disponíveis:')
        for idx, professor in enumerate(professores, start=1):
            print(f"{idx}. {professor['nome']} (Código: {professor['Código de Matrícula']})")
        
        escolha = input('Você deseja adicionar um professor existente ou um novo? [novo] [existente]\n')
        if escolha == 'existente':
            codigo_professor = input('Digite o código do professor que deseja adicionar:\n ')
            professor = next((prof for prof in professores if prof['Código de Matrícula'] == codigo_professor), None)
            if not professor:
                print("Código inválido. Vamos cadastrar um novo professor.")
                from professores import cadastrar_professor
                professor = cadastrar_professor()
        else:
            from professores import cadastrar_professor
            professor = cadastrar_professor()
    else:
        print('Ainda não existem professores cadastrados, vamos cadastrar um agora!')
        from professores import cadastrar_professor
        professor = cadastrar_professor()
    
    disciplina = {
        'Nome da Disciplina': nome,
        'Código da Disciplina': codigo,
        'Carga Horária da Disciplina': carga,
        'Professor da Disciplina': professor['nome'],
        'Código do professor': professor['Código de Matrícula']
    }
    professor['Disciplinas'].append(disciplina)

    return disciplina
