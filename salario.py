#Calculo de salário baseado na quantia de horas trabalhadas em determinado mês e no quanto recebe por hora trabalhadas.

ganho_por_hora = int(input("Informe o quanto você ganha por hora"))

horas_trabalhadas = float(input("Informe quantas horas você trabalhou no total deste mês"))

calculoSalarial = ganho_por_hora * horas_trabalhadas

print("O seu salário baseado no seu ganho por hora de {} junto de suas horas trabalhadas {}, corresponde à {}R$".format(ganho_por_hora,horas_trabalhadas,calculoSalarial))


