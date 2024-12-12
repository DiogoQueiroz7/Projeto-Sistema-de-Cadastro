from codigo_matricula import gerar_codigo_matricula
from cadastro_professores import listar_professores, professores


print('Olá, este é o cadastro de disciplinas, vamos começar!')

def cadastrar_disc():
    nome =  input('Digite o nome da disciplina: \n')
    codigo = gerar_codigo_matricula()
    carga = int(input('Digite a carga horária da disciplina: \n'))
    
    if professores:
        print('Professores disponiveis')
        listar_professores()
        escolha = input('Você deseja adicionar um professor existente ou um novo? [novo] [existente]\n')
        if escolha == 'existente':
            code_professor = int(input('Digite o código do professor que deseja adicionar:\n ')) -1
            professor = professores[code_professor]
        else:
            from cadastro_professores import cadastrar_professor
            professor = cadastrar_professor()
        
    else:
        print('Ainda não existemm professores cadastrados, vamos cadastrar um agora!')
        from cadastro_professores import cadastrar_professor
        professor = cadastrar_professor()
        
        disciplina = {
            'Nome da Disciplina': nome,
            'Código da Disciplina': codigo,
            'Carga Horária da Disciplina': carga,
            'Professor da Disciplina': professor['nome'],
            'Código do professor': professor['Código de Matricula']
        }
        professor['Disciplinas'].append(disciplina)  

    return disciplina

disciplinas = []

while True:
    disciplinas.append(cadastrar_disc())
    resposta = (input('Você deseja adicionar mais alguma disciplina? [sim] [nao]\n'))
    if resposta == 'nao':
        print('Tá bom, tenha um bom dia!')
        break
    elif resposta != 'sim':
        print('Você não digitou nenhuma opção, digite [sim] ou [nao]')
        
print('DISCIPLINAS CADASTRADAS')
for disc in disciplinas:
    print(disc)
    