def somar_todos_os_numeros (*numeros):
    total = 0
    for num in numeros:
     total += num
    return total
print(somar_todos_os_numeros (1, 2, 3))