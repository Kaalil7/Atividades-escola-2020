import os
print(35*"-")
print("Equação de primeiro grau em Python")
print(35*"-")

equa = input("Digite qual equação deseja:\n\n 1 - f(x) = ax + b + c = 0\n 2 - f(x) = ax - b + c = 0 \n 3 - f(x) = -ax + b + c = 0\n 4 - f(x) = ax - b - c = 0\n 5 - f(x) = -ax - b - c = 0\n")

os.system("clear")

if equa == "1":
  print("f(x) = ax + b = 0")
  ax = int(input("Digite o valor de A: "))
  b = int(input("Digite o valor de B: "))
  c = int(input("Digite o valor de C: "))
  equa1 = (b + c) / ax
  equa2 = equa1 / ax
  print(f"O resultado de sua equação de primeiro grau é: {equa2}")
if equa == "2":
  print("f(x) = ax - b = 0")
  ax = int(input("Digite o valor de A: "))
  b = int(input("Digite o valor de B: "))
  c = int(input("Digite o valor de C: "))
  equa2 = (-b + c) / ax
  print(f"O resultado de sua equação de primeiro grau é: {equa2}")
if equa == "3":
  print("f(x) = -ax + b = 0")
  ax = int(input("Digite o valor de A: "))
  b = int(input("Digite o valor de B: "))
  c = int(input("Digite o valor de C: "))
  equa2 = (b + c) / -ax
  print(f"O resultado de sua equação de primeiro grau é: {equa2}")
if equa == "4":
  print("f(x) = ax - b - c = 0")
  ax = int(input("Digite o valor de A: "))
  b = int(input("Digite o valor de B: "))
  c = int(input("Digite o valor de C: "))
  equa2 = (-b - c) / ax
  print(f"O resultado de sua equação de primeiro grau é: {equa2}")
if equa == "5":
  print("f(x) = -ax - b - c = 0")
  ax = int(input("Digite o valor de A: "))
  b = int(input("Digite o valor de B: "))
  c = int(input("Digite o valor de C: "))
  equa2 = (-b - c) / -ax
  print(f"O resultado de sua equação de primeiro grau é: {equa2}")




  




