import os
print(25*"-")
print("Calcule seu IMC!")
print(25*"-")

nome = input("\nDigite seu nome: ")
idade = int(input("\nDigite sua idade: "))
peso = float(input("\nDigite seu peso: "))
altura = float(input("\nDigite sua altura: "))

os.system("clear")

imc = peso/altura**2

if imc < 16:
  imc2 = ("Magreza grave")
elif imc < 17:
  imc2 = ("Megreza moderada")
elif imc < 18.5:
  imc2 = ("Magreza leve")
elif imc < 25:
  imc2 = "Saudável"
elif imc < 30:
  imc2 = "Sobrepeso"
elif imc < 35:
  imc2 = "Obesidade Grau I"
elif imc < 40:
  imc2 = "Obsesidade Grau II"
else:
  imc2 = "Obesidade Grau III"

print(f"Seu nome é {nome}, tem {idade} anos de idade {peso} de peso, {altura} de altura e \nseu IMC é {imc} kg/m², considerado como: {imc2}")
