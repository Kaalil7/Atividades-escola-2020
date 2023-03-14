from random import randint
from time import sleep

lista = ("Pedra", "Papel", "Tesoura")

computador = randint(0, 2)

print("=-"*20)
print("Bem vindo ao Pedra, papel e tesoura!")
print("=-"*20)


perguntar = int(input("Escolha:\n\n [0] Pedra\n [1] Papel\n [2] Tesoura\n\n"))


sleep(1)
print("\nJO\n")
print("KEN\n")
sleep(1)
print("PO!\n")

print("=-"*20)
print("O jogador escolheu: {}".format(lista[perguntar]))
print("O computador escolheu {}".format(lista[computador]))
print("=-"*20)

if (computador == 0):
  if(perguntar == 0):
    print("EMPATE!")
  elif (perguntar == 1):
    print("O jogador venceu!")
  elif (perguntar == 2):
    print("O computador venceu!")
  else:
    print("Erro. Tente novamente!")
    
if (computador == 1):
  if (perguntar == 0):
    print("O computador venceu!")
  elif (perguntar == 1):
    print("EMPATE!")
  elif (perguntar == 2):
    print("O jogador venceu!")
  else:
    print("Erro. Tente novamente")

if (computador == 2):
  if (perguntar == 0):
    print("O jogador venceu!")
  elif (perguntar == 1):
    print("O computador venceu!")
  elif (perguntar == 2):
    print("EMPATE!")
  else:
    print("Erro. Tente novamente")








