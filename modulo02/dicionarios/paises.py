paises = {"Russia":"Moscou", "Brasil":"Brasília", "Índia":"Nova Deli", "China":"Pequim", "África do Sul":"Pretória"
}

print("Países disponíveis:", ', '.join(paises.keys()))
usuario = input("Digite um país e voce terá sua capital: ")
print(f"A capital do país {usuario} é {paises.get(usuario, 'País não encontrado no dicionário')}")

