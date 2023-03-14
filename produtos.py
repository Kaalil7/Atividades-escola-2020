preco = 1
acm50 = contador = cont = soma = maior = menor = 0

while preco != 999:
  produto = str(input("Digite o nome do produto: "))
  preco = float(input("Digite o preço R$: ".replace(',','.')))
  soma += preco
  cont += 1
  if cont == 1:
    maior = menor = preco
  else:
    if preco < menor:
      menor = preco
    if preco > maior:
      maior = preco
  if maior > 1000:
    contador += 1
    acm50 += preco
  print(f"{produto} R${preco:.2f}".replace('.',','))
  print(f"Total: R${soma:.2f}".replace('.',','))
  print(f"Produto: {acm50}, {contador} acima de R$1000,00")
  print(f"Menor preço: {menor}, maior preço: {maior}")
