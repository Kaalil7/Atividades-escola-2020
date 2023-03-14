
media = int(input("Digite quantas notas serão calculadas: "))
i = 0
soma = 0
for i in range(1, media + 1):
  nota = float(input("Nota {0}: ".format(i)))
  print(nota)
  soma += nota
media1 = soma / i
print(25*"-")
print("A média final foi de {0}".format(media1))
print(25*"-")


  
