cont = soma = cont2 = soma2 = sexo = 0
pergunta = int(input("Deseja saber o sexo de quantas pessoas: "))

while cont2 != pergunta:
  cont2 += 1
  resposta = input('F - Femnino e M - Masculino: ')
  if resposta == 'M' or resposta == "m":
    print('Masculina')
  else:
    if resposta == 'F' or resposta == "f":
        print('Feminina')
    else:
        print('Você não digitou M ou F')
print(5*"-")
print("Fim!")
print(5*"-")
    
     
    

