#Área do quadrado, e o dobro da área.
from math import pow

alturaDoQuadrado = float(input("Informe o valor da altura do quadrado a ser calculado"))

area = pow(alturaDoQuadrado,2)

dobroDaArea = pow(area,2)

print("A altura informada foi de {}, e sua área corresponde à {}".format(alturaDoQuadrado,area))
print("\n")
print("O dobro da área corresponde à: ",dobroDaArea)