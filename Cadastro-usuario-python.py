import os
print("Olá, bem vindo ao World Of War!")
print("-------------------------------")
personagem = input("Vamos criar seu personagem, qual a cor de seu uniforme? \n 1 - Azul\n 2 - Verde\n 3 - Amarelo\n 4 - Vermelho\n")
os.system("clear") or None
lado = input("Qual lado você irá apoiar?\n 1 - Aliados\n 2 - Eixo\n")
os.system("clear") or None
exercito = input("Você irá jogar do que?\n 1 - Terrestre\n 2 - Aérea\n 3 - Marítima\n")
os.system("clear") or None
print("Agora vamos fazer seu cadastro: ")
print("--------------------------------")
email = input("Digite seu e-mail\n")
os.system("clear") or None
email2 = input("Confirme seu e-mai\n")
os.system("clear") or None
senha = input("Digite sua senha\n")
os.system("clear") or None
senha2 = input("Confirme sua senha\n")
if(email == email2):
  if(senha == senha2):
    print("Parabéns, cadastro concluido!")
  else:
    print("Verifique sua senha!")
else:
  print("Verifique seu e-mail!")


