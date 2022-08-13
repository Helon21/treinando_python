import math 

#1 numero real e 2 inteiros, após isso alguns calculos serão feitos.
numInteiro = int(input("Informe um número inteiro"))
numInteiro2 = int(input("Informe um outro número inteiro"))
numReal = float(input("Informe um número real"))

#produto do dobro do primeiro (numInteiro) com metade do segundo (numInteiro2)

produto = (numInteiro2 * 2) / (numInteiro2 / 2)

print("O produto resultante do dobro do primeiro número com metade do segundo número tem como resultado o valor: ",produto)

#Soma do triplo do primeiro número (numInteiro) com o terceiro (numReal)

soma = (numInteiro * 3) + numReal

print("A soma do triplo do primeiro número com o terceiro número equivale à: ",soma)

#Terceiro número elevado ao cubo

cubo = pow(numReal,3)

print("O número {}, elevado ao cubo, equivale à {}".format(numReal,cubo))