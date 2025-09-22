conversao_para_metros = {"metros": 1,"quilômetros": 1000}

quantidade = float(input("Digite a quantidade: "))
unidade_origem = input("Digite a unidade de origem (metros ou quilômetros): ").strip().lower()
unidade_destino = input("Digite a unidade de destino (metros ou quilômetros): ").strip().lower()

if unidade_origem in conversao_para_metros and unidade_destino in conversao_para_metros:
    em_metros = quantidade * conversao_para_metros[unidade_origem]
    resultado = em_metros / conversao_para_metros[unidade_destino]
    print(f"{quantidade} {unidade_origem} equivalem a {resultado} {unidade_destino}")
else:
    print("Unidade inválida. Tente novamente.")