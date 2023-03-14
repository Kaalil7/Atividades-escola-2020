import os

print(25*"-")
print("Aula 1 - Criar algoritmo")
print(25*"-")

pergunta = input("O que deseja calcular?\n\n 1 - Adição\n 2 - Subtração\n 3 - Multiplicação\n 4 - Divisão\n 5 - Exponenciação\n")

if pergunta == "1" or pergunta == "Adição":
  os.system("clear")
  print("Ok! Vamos lá!")
  num1 = int(input("Digite um número: "))
  num2 = int(input("Digite um outro número: "))
  resul = num1 + num2 
  print("O resultado dessa adição é", resul)
elif pergunta == "2" or pergunta == "Subtração":
  os.system("clear")
  print("Ok! Vamos lá!")
  num1 = int(input("Digite um número: "))
  num2 = int(input("Digite um outro número: "))
  resul = num1 - num2
  print("O resultado desta subtração é", resul )
elif pergunta == "3" or pergunta == "Multiplicação":
  os.system("clear")
  print("Ok! Vamos lá!")
  num1 = int(input("Digite um número: "))
  num2 = int(input("Digite um outro número: "))
  resul = num1 * num2 
  print("O resultado desta Multiplicação é", resul)
elif pergunta == "4" or pergunta == "Divisão":
  os.system("clear")
  print("Ok! Vamos lá!")
  num1 = int(input("Digite um número: "))
  num2 = int(input("Digite um outro número: "))
  resul = num1 / num2
  resto = num1 % num2
  print("O resultado desta divisão é", resul )
  print("O resto dessa divisão é ", resto)
elif pergunta == "5" or pergunta == "Exponenciação":
  os.system("clear")
  print("Ok! Vamos lá!")
  num1 = int(input("Digite um número: "))
  num2 = int(input("Digite um outro número para ser o expoente: "))
  resul = num1 ** num2
  print("O resultado dessa exponenciação é", resul)
else:
  print("Erro! Tente novamente!")






