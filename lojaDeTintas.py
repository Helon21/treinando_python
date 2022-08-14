from math import pow
#Calcula quantas latas de tinta deverão ser compradas e informa o preço total

areaMetrosQuadrados = float(input("Informe a área em metros quadrados, que será pintada"))

latasLitros = 18 #cada litro rende 3 metros quadrados
custoPorLata = 80.00
qtdeLatas = areaMetrosQuadrados / (latasLitros / 3)
latasComprar = (areaMetrosQuadrados / qtdeLatas) * 80.00

print("A área a ser pintada é de {} m² e a quantia de latas a serem usadas é de {}. O custo total é: {:.2f}".format(areaMetrosQuadrados,latasComprar,))

