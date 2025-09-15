
while True:
        lado_A = input("Digite o valor do lado A: ")
        lado_B = input("Digite o valor do lado B: ")
        lado_C = input("Digite o valor do lado C: ")
    
       
        if not (lado_A.isdigit() and lado_B.isdigit() and lado_C.isdigit()):
            print("Todos os lados devem ser números inteiros positivos.")
            continue
    
        lado_A = int(lado_A)
        lado_B = int(lado_B)
        lado_C = int(lado_C)
    
        if lado_A < 0 or lado_B < 0 or lado_C < 0:
            print("Os lados devem ser maiores que zero.")
            continue


        if lado_A > lado_B + lado_C or lado_B > lado_A + lado_C or lado_C > lado_A + lado_B:
            print("Os valores não formam um triângulo .")
            continue
    
        if lado_A < abs(lado_B - lado_C) or lado_B < abs(lado_A - lado_C) or lado_C < abs(lado_A - lado_B):
            print("Os valores não formam um triângulo .")
            continue
    
        print("Os valores formam um triângulo.") 
        break
 
  
      