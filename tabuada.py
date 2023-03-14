print(8*"-")
print("Tabuada")
print(8*"-")

i = 0

while i < 10:
  i += 1
  j = 0
  while j < 10:
    j += 1
    r = i * j
    print("{0} x {1} = {2}".format(i, j, r))
