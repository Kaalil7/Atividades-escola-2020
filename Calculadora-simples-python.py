print("===============================")
print("Isto é uma simples calculadora.")
print("===============================")

valor1 = float(input("Digite um valor: "))
operador = input("Digite o operador desejado: ")
valor2 = float(input("Digite um outro valor: "))
input("Digite o sinal de igual: ")

if (operador == "+"):
  resultado = valor1 + valor2
elif (operador == "-"):
  resultado = valor1 - valor2
elif (operador == "*"):
  resultado = valor1 * valor2
elif (operador == "/"):
  resultado = valor1 / valor2
else:
  print("Ocorreu um erro. Tente outro operador.")
print("O resultado é de ", resultado)
