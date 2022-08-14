#calcula o tempo (minutos) que levará o download

tamanho = float(input("Informe o tamanho total do arquivo em MB"))

velocidade = float(input("Informe a velocidade da sua internet em Mbps"))

tempo = (tamanho / velocidade) * 60 

print("O tempo estimado é de {} minutos".format(tempo))