from codigo_matricula import gerar_codigo_matricula
print('Olá, este é o cadastro de alunos, vamos começar! ')
alunos = []
def cadastrar_aluno():
    nome = input(str('Qual o nome do aluno? \n'))
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
    return {'nome': nome,  
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
                }
            }
def listar_alunos():
    if not alunos: 
        print('Poxa, não tem nenhum aluno cadastrado') 
        return 
    for idx, aluno in enumerate(alunos, start=1): 
        print(f"{idx}. {aluno['nome']}")

