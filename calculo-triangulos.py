
base = float(input("Digite a base da figura: "))
altura = float(input("Digite a altura da figura: "))

area = (base * altura) / 2
hipotenusa = (base ** 2 + altura ** 2)
hipotenusa0 = hipotenusa ** 0.5 
perimetro = base + altura + hipotenusa0

print("A área do Triângulo é igual a {0}, o perimetro é  igual a {1:.2f} e a Hipotenusa é igual a {2:.2f}".format(area, perimetro, hipotenusa0))
