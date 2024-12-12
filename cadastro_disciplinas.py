from codigo_matricula import gerar_codigo_matricula
from cadastro_professores import cadastrar_professor, listar_professores, professores


print('Olá, este é o cadastro de disciplinas, vamos começar!')

def cadastrar_disc():
    nome =  str(input('Digite o nome da disciplina: \n'))
    codigo = gerar_codigo_matricula()
    carga = int(input('Digite a carga horária da disciplina: \n'))
    
    if professores:
        print('Professores disponiveis')
        print(listar_professores())
        escolha = input('Você deseja adicionar um professor existente ou um novo? [novo] [existente]\n')
        if escolha == 'existente':
            code_professor = int(input('Digite o código do professor que deseja adicionar:\n ')) -1
            professor = professores[code_professor]
        else:
            professor = cadastrar_professor()
        
    else:
        print('Ainda não existemm professores cadastrados, vamos cadastrar um agora!')
        professor = cadastrar_professor()
        
    
    