
pecas = 4500
defeito = 180

porcentagem = defeito / (pecas / 100)
if porcentagem < 4:
  print("Aprovado")
else:
  print("Não foi aprovado")
print(porcentagem)
