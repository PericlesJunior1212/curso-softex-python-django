                            ##Desafio do Triângulo##
while True:

  lado_A = input("Digite o valor do lado A: ")
  lado_B = input("Digite o valor do lado B: ")
  lado_C = input("Digite o valor do lado C: ")
  
  lado_A = int(lado_A)
  lado_B = int(lado_B) 
  lado_C = int(lado_C)

  if lado_A <= 0 or lado_B <= 0 or lado_C <= 0:
      print("Os lados devem ser maiores que zero.")
  elif lado_A > lado_B + lado_C or lado_B > lado_A + lado_C or lado_C > lado_B + lado_A:
      print("Os valores não formam um triângulo.")
  else:
      print("Os valores formam um triângulo.")
     
      