#calculo de salário, mostrará o salário bruto, e o salário líquido, junto com os descontos por impostos

ganhoPorHora = float(input("Informe o quanto você ganha por hora"))

horasTrabalhadasMes = int(input("Informe quantas horas foram trabalhadas no mês"))

salarioBruto = ganhoPorHora * horasTrabalhadasMes

imposto_renda = salarioBruto * 11/100

iNSS = salarioBruto * 8/100 

sindicato = salarioBruto * 5/100

salarioLiquido = salarioBruto - imposto_renda - iNSS - sindicato

print("O seu salário bruto é de {}R$. Seu salário líquido corresponde à {}R$".format(salarioBruto, salarioLiquido))
print("\n")
print("Os descontos aplicados no seu salário foram {}'%' de Imposto de Renda, {}'%' de INSS e {}'%' de sindicato".format(imposto_renda, iNSS, sindicato))