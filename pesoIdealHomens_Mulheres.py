#calculo de peso ideal para homens e mulheres (atividade da lista de exercicios)

h = float(input("Informe sua altura")) # h armazena altura

calculoPesoHomens = (72.7 * h) - 58
calculoPesoMulheres = (62.1 * h) - 44.7

print("Com base na altura informada {}, o peso ideal é de {:.2f}Kg, para homens desta altura".format(h,calculoPesoHomens))
print("\n")
print("Com base na altura informada {}, o peso ideal é de {:.2f}Kg, para mulheres desta altura".format(h,calculoPesoMulheres))

