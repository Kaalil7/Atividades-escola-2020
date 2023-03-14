num1 = 0
anterior = 0
proximo = 0
stop = False

while not stop:
    num1 = int(input("Digite algum núnero: "))
    while (proximo < num1):
     print(proximo)
     proximo = proximo + anterior
     anterior = proximo - anterior
     if(proximo == 0):
       proximo = proximo + 1
     if input("Deseja sair (Y/N) ? ").lower() == "y":
       stop = True
