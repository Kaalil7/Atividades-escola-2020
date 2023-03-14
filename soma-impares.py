
num1 = int(input("Digite um número: "))
num2 = int(input("Digite um outro número: "))

if num1 and num2 % 2 >= 1:
  resul = num1 + num2
  print("Como estes números são impares, o resultado é {0}".format(resul))
else:
  print("Estes números não são impares.")
