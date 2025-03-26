# Criar um cadastro de alunos com as seguintes informações:
# Nome, idade e nota. Armazena os dados em uma lista de dicionários.
# Calcula a média da turma. Permite listar todos os alunos e buscar um aluno específico.

def cadastrar_aluno(alunos):
    nome = input("Digite o nome do aluno: ")
    idade = int(input("Digite a idade do aluno: "))
    nota = float(input("Digite a nota do aluno: "))
    alunos.append({"nome": nome, "idade": idade, "nota": nota})
    print("Aluno cadastrado com sucesso!")

def calcular_media(alunos):
    if not alunos:
        print("Nenhum aluno cadastrado.")
        return
    media = sum(aluno["nota"] for aluno in alunos) / len(alunos)
    print(f"A média da turma é: {media:.2f}")

def listar_alunos(alunos):
    if not alunos:
        print("Nenhum aluno cadastrado.")
        return
    print("Lista de alunos:")
    for aluno in alunos:
        print(f"Nome: {aluno['nome']}, Idade: {aluno['idade']}, Nota: {aluno['nota']}")

def buscar_aluno(alunos):
    nome = input("Digite o nome do aluno que deseja buscar: ")
    for aluno in alunos:
        if aluno["nome"].lower() == nome.lower():
            print(f"Aluno encontrado: Nome: {aluno['nome']}, Idade: {aluno['idade']}, Nota: {aluno['nota']}")
            return
    print("Aluno não encontrado.")

def menu():
    alunos = []
    while True:
        print("\nMenu:")
        print("1. Cadastrar aluno")
        print("2. Calcular média da turma")
        print("3. Listar todos os alunos")
        print("4. Buscar aluno específico")
        print("5. Sair")
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            cadastrar_aluno(alunos)
        elif opcao == "2":
            calcular_media(alunos)
        elif opcao == "3":
            listar_alunos(alunos)
        elif opcao == "4":
            buscar_aluno(alunos)
        elif opcao == "5":
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()