tamanho = float(input("Entre com o tamanho da área: "))

litros = tamanho / 6
latas = litros / 18

if latas % 18 != 0:
    latas += 1
preco = latas * 80

galoes = litros / 3.6
if galoes % 3.6 != 0:
    galoes += 1
preco2 = galoes * 25

# mistura de latas e galoes
mistura_lata = int(litros / 18.0)
mistura_galao = int((litros - (mistura_lata * 18)) / 3.6)

if litros - (mistura_lata * 18) % 3.6 != 0:
    mistura_galao += 1

print("Apenas latas de 18 litros: {:.2f} latas, preço: {:.2f}".format(latas,preco))
print("Apenas galões de 3.6 litros: {:.2f} , galoes, preço: {:.2f}".format(galoes,preco2))
print("Mistura: {:.2f} latas e {:.2f} galoes = {:.2f}".format(mistura_lata, mistura_galao, ((mistura_lata * 80) + (mistura_galao * 25))))