#Converte a temperatura de farenheits para celsius

farenheit = float(input("Informe a temperatura em graus farenheit"))

celsius = 5 * ( (farenheit - 32) / 9 )

print("A temperatura informada em farenheit foi de {}, após a conversão, o resultado em graus celsius foi de {:.2f}".format(farenheit,celsius))
