'''Você foi contratado(a) para desenvolver um programa que gerencie um dicionário de alunos onde a 
chave deste dicionário é o número de matrícula dos próprios alunos. O programa deve permitir adicionar, remover, 
atualizar e listar os alunos.
Para isso, você deve implementar um módulo que contém as seguintes funções:
AdicionarAluno(): Solicita ao usuário que digite o nome e o número de matrícula de um aluno e adicione-o ao dicionário 
de alunos.
RemoverAluno(): Solicita ao usuário que digite o número de matrícula de um aluno e remove-o do dicionário de alunos.
AtualizarAluno(): Solicita ao usuário que digite o número de matrícula de um aluno e atualize o nome desse aluno 
no dicionário .
VerAlunos(): Lista todos os alunos cadastrados, exibindo o número de matrícula e o nome de cada um.
Lembre Se de Modularizar o código'''

alunos = {}

def AdicionarAluno():
    matricula = input("Digite o número de matrícula do aluno: ")
    nome = input("Digite o nome do aluno: ")
    alunos[matricula] = nome
    print(f"Aluno adicionado: {nome} (Matrícula: {matricula})")

def RemoverAluno():
    matricula = input("Digite o número de matrícula do aluno a ser removido: ")
    if matricula in alunos:
        nome = alunos.pop(matricula)
        print(f"Aluno removido: {nome} (Matrícula: {matricula})")
    else:
        print(f"Aluno com matrícula {matricula} não encontrado.")

def AtualizarAluno():
    matricula = input("Digite o número de matrícula do aluno a ser atualizado: ")
    if matricula in alunos:
        novo_nome = input("Digite o novo nome do aluno: ")
        alunos[matricula] = novo_nome
        print(f"Nome do aluno atualizado para: {novo_nome} (Matrícula: {matricula})")
    else:
        print(f"Aluno com matrícula {matricula} não encontrado.")

def VerAlunos():
    if not alunos:
        print("Nenhum aluno cadastrado.")
    else:
        print("Lista de Alunos:")
        for matricula, nome in alunos.items():
            print(f"Matrícula: {matricula}, Nome: {nome}")

opcao = None
while opcao != "5":
    print("\nMenu:")
    print("1. Adicionar Aluno")
    print("2. Remover Aluno")
    print("3. Atualizar Aluno")
    print("4. Ver Alunos")
    print("5. Sair")

    opcao = input("Escolha uma opção (1-5): ")

    if opcao == "1":
        AdicionarAluno()
    elif opcao == "2":
        RemoverAluno()
    elif opcao == "3":
        AtualizarAluno()
    elif opcao == "4":
        VerAlunos()
    elif opcao == "5":
        print("Programa encerrado.")
    else:
        print("Opção inválida. Tente novamente.")