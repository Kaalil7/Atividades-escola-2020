import os

print("Calculadora")

numerador = float(input("Digite o numerador: "))
denominador = float(input("Digite o denominador: "))
operador = str(input("Digite o operador: "))

if operador == "+":
  resultado = numerador + denominador
  print(f"A soma entre ambos é igual a {resultado}")
  print("Até logo")
elif operador == "-":
  resultado = numerador - denominador
  print(f"A subtração entre ambos é igual a {resultado}")
  print("Até logo")
elif operador == "*":
  print(f"A multiplicação entre ambos é igual a {resultado}")
  print("Até logo")
elif operador == "/":
  resultado = numerador/denominador
  print(f"A divisão entre ambos é igual a {resultado}")
  print("Até logo") 
else:
  print("Até logo")
