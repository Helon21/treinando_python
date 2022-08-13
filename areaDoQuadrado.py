#Área do quadrado, e o dobro da área.
from math import pow

altura = float(input("Informe o valor da altura do quadrado a ser calculado"))

area = pow(altura,2)

dobroDaArea = pow(area,2)

print("A altura informada foi de {}, e sua área corresponde à {}".format(altura,area))
print("\n")
print("O dobro da área corresponde à: ",dobroDaArea)