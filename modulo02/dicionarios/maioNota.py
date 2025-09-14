notas = {"João": 8.5, "Maria": 9.0, "Pedro": 7.5, "Ana": 10.0, "Lucas": 6.5}
for alunos, nota in notas.items():


    if nota >= 7.0:
        print(f"Aluno: {alunos} - Nota: {nota} - Aprovado")
    else:
        print(f"Aluno: {alunos} - Nota: {nota} - Reprovado")