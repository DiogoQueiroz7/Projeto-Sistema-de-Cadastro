from codigo_matricula import gerar_codigo_matricula

professores = []

def cadastrar_professor():
    print("Olá Professor, vamos te cadastrar agora!")
    nome = input('Qual o nome do professor? \n')
    nasc = input('Informe sua data de nascimento (dd/mm/aa): \n')
    sexo = input('Qual seu sexo? [masculino] [feminino]\n')
    tel = input('Me informe seu número de telefone (**)*********: \n')
    email = input('Digite seu melhor email:\n')
    matricula = gerar_codigo_matricula()
    cidade = input('Qual o nome da sua cidade? \n')
    estado = input('Qual seu estado?\n')
    rua = input('Me informe o nome da sua rua: \n')
    num = input('Qual o número da sua residência? \n')
    bairro = input('Qual o nome do seu bairro? \n')

    professor = {
        'nome': nome,  
        'data de nascimento': nasc, 
        'sexo': sexo, 
        'Telefone': tel, 
        'Email': email,
        'Código de Matrícula': matricula,
        'endereço': { 
            'Cidade': cidade,
            'Estado': estado,
            'Rua': rua, 
            'Número': num,
            'Bairro': bairro
        },
        'Disciplinas': []
    }

    professores.append(professor)
    return professor

def listar_professores():
    if not professores:
        print('Poxa, não tem nenhum professor cadastrado')
        return
    for idx, professor in enumerate(professores, start=1):
        print(f"{idx}. {professor['nome']}")
