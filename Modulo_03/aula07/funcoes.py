# funcoes.py
def somar(a, b):
    return a + b
    
def subtrair(a, b):
    return a - b
    
def processar_lista(lista):
    
    """Ordena uma lista, levantando erro se vazia."""
        
    if not lista:
        raise ValueError("Lista não pode ser vazia.")
        # Supondo que a implementação correta seja ordenar
    return sorted(lista)


def buscar_usuario(usuarios: list, id_usuario: int):
    """Busca um usuário em uma lista de dicionários pelo ID.

    Retorna o dicionário do usuário quando o campo 'id' coincide com
    `id_usuario`. Se nenhum usuário for encontrado, retorna None.
    """
    for usuario in usuarios:
        if usuario.get('id') == id_usuario:
            return usuario

    # retorna None somente depois de verificar todos os usuários
    return None