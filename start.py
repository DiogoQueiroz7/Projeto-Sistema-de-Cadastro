import professores
import disciplinas
import alunos
import codigo_matricula
import turma 

def menu():
    print('************************SISTEMA DE CADASTRO ESCOLAR************************')
    print('Olá, este é o sistema de CADASTRO ESCOLAR')
    print('Selecione a Opção desejada')
    print('[1] CADASTRAR ALUNO') 
    print('[2] CADASTRAR PROFESSOR')
    print('[3] CADASTRAR DISCIPLINA')
    print('[4] CADASTRAR TURMA')
    print('[5] MATRICULAR ALUNO')
    print('[6] ALOCAR PROFESSOR')
    print('[7] ALOCAR DISCIPLINA EM TURMA')
    print('[0] SAIR')
    print('***********************************************************************')

def main():
    while True:
        menu()
        resposta = input('Digite a opção que deseja realizar: ').strip()
        
        if resposta == '1':
            alunos.cadastrar_aluno()
        elif resposta == '2':
            professores.cadastrar_professor()
        elif resposta == '3':
            disciplinas.cadastrar_disc()
        elif resposta == '4':
            turma.cadastrar_turma()  
        elif resposta == '5':
            turma.matricular_aluno()  
        elif resposta == '6':
            turma.alocar_professor() 
        elif resposta == '7':
            turma.alocar_disciplina()  
        elif resposta == '0':
            print('Saindo do sistema. Até logo!')
            break
        else:
            print('Você não digitou uma opção válida. Tente novamente.')

if __name__ == "__main__":
    main()
