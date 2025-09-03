notas = [("Ana","9.5"),("João","8.0"),("Pedro","7.5"),("Ana","10.0"),("Carlos","6.5"),("Maria","10.0")]
maior = 0
alunos_maior = set()
alunos_menor = set()
for nome, nota in notas:
    if maior > notas:
        maior = notas
        if nota == maior:
            alunos_maior.add(nome)
    if nota < 7.0:
        alunos_menor.add(nome)
        alunos_maior = tuple (alunos_maior)
print(f"Amaior nota foi: {maior}")
print(f"Alunos que tiraram maior notas : {alunos_maior}")