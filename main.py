num_alunos = int(input("Digite a quantidade de alunos: "))

media_turma = 0

for aluno in range(1, num_alunos + 1):
    print(f"\nAluno {aluno}")
    nome = input("Digite o nome do aluno: ")

    notas = []
    for nota_aluno in range(1, 4):
        nota = float(input(f"Digite a nota {nota_aluno} do aluno {nome}: "))
        notas.append(nota)
    
    media_aluno = sum(notas) / 3
    media_turma += media_aluno

    if media_aluno >= 7:
        print(f"O aluno {nome} está aprovado com a média de {media_aluno}")
    else:
        print(f"O aluno {nome} está reprovado com a média de {media_aluno}")

    print(f"\nNome: {nome}")
    print(f"\nNotas: {notas}")
    print(f"\nMédia: {media_aluno:.2f}")
    print(f"\nStatus: {media_aluno:.2f}")
    
media_geral = media_turma / num_alunos
print(f"\nMédia da turma: {media_geral:.2f}")