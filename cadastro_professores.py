from codigo_matricula import gerar_codigo_matricula
from cadastro_disciplinas import cadastrar_disc

print("Olá Professor, vamos te cadastrar agora! ")
professores = []
def cadastrar_professor():
    nome = input(str('Qual o nome do professor? \n'))
    nasc = input('Infome sua data de nascimento (dd/mm/aa): \n')
    sexo = input(str('Qual seu sexo? [masculino] [feminino]\n'))
    tel = input('Me informe seu  número de telefone (**)*********: \n')
    email = input(str('Digite seu melhor email:\n'))
    matricula = gerar_codigo_matricula()
    cidade = input('Qual o nome da sua cidade? \n')
    estado = input('Qual seu estado?\n')
    rua = input('Me informe o nome da sua rua: \n')
    num = input('Qual o número da sua residência? \n')
    bairro = input('Qual o nome do seu bairro? \n')
    
    disc_professor = []
    while adicionar_disciplina.lower() == 'sim': 
        disc_professor.append(cadastrar_disc()) 
        adicionar_disciplina = input('Deseja adicionar mais uma disciplina a este professor? [sim] [nao]\n')
    
    
    professor = {'nome': nome,  
            'data de nascimento': nasc, 
            'sexo': sexo, 
            'Telefone': tel, 
            'Email': email,
            'Código de Matricula': matricula,
            'endereço': { 
                'Cidade': cidade,
                'Estado': estado,
                'Rua': rua, 
                'Número': num,
                'Bairro': bairro
                },
            'Disciplinas': disc_professor
            }
    
    professores.append(professor)
    return professor
def listar_professores(): 
    print("Professores cadastrados:") 
    for idx, professor in enumerate(professores, start=1): 
        print(f"{idx}. {professor['nome']}")