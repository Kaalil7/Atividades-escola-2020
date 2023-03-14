soma = 0
for i in range(1, 7):
  num = int(input("Digite o número {0}: ".format(i)))
  if num % 2 >= 1:
    print("É um número par.")
  else:
    soma += num
print("A soma dos números pares é {0}.".format(soma))
