#Converte a temperatura de celsius para farenheit

celsius = float(input("Informe a temperatura em graus celsius"))

farenheit = celsius * 1.8 + 32

print("A temperatura informada em graus celsius foi de {} ºC, após convertida obtivemos um resultado de {:.2f}ºF".format(celsius,farenheit))