notas = [("Ana","9.5"),("João","8.0"),("Pedro","7.5"),("Ana","10.0"),("Carlos","6.5"),("Maria","10.0")]

maior = 0.0
alunos_maior = set()
alunos_menor = set()

for nome, nota in notas:
    nota = float(nota)
    if nota > maior:
        maior = nota
        alunos_maior = {nome}
    elif nota == maior:
        alunos_maior.add(nome)
    if nota < 7.0:
        alunos_menor.add(nome)

print(f"A maior nota foi: {maior}")
print(f"Alunos que tiraram a maior nota: {alunos_maior}")
print(f"Alunos com nota menor que 7: {alunos_menor}")