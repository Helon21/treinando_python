#calcular o excendente de kilos de peixe, ao passar de 50 a multa é de 4 reais por kg excedente


pesoPeixes = float(input("Informe o peso total de todos os peixes juntos, que foram pescados"))

if(pesoPeixes >= 51):
    excedente = float(input("Informe quantos kilos se passaram acima dos 50 permitidos"))
    multa = 4.00 * excedente
    print("O valor dá multa aplicada pelo excedente de {}Kg, corresponde à: {}".format(excedente,multa))

else:
    print("Não é necessário para multa, o peso está dentro do limite")
