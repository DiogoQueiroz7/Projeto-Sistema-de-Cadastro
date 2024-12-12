from codigo_matricula import gerar_codigo_matricula


print('Olá, este é o cadastro de disciplinas, vamos começar!')

def cadastrar_disc():
    nome =  str(input('Digite o nome da disciplina: \n'))
    codigo = gerar_codigo_matricula()
    carga = int(input('Digite a carga horária da disciplina: \n'))
    
    return {
        'Nome da Disciplina': nome, 
        'Código da disciplina': codigo,
        'Carga Horária da Disciplina': carga,
    }
    