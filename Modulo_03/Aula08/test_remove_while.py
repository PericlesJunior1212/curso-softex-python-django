def test_remove():
    from RemoveWhile import remove

    lista = ["Python", "Java", "C++", "JavaScript", "Ruby", "Go", "PHP"]
    result_esperado = ["Python", "Java", "C++", "JavaScript", "Ruby", "Go", "PHP"]

    assert remove(lista) == result_esperado
