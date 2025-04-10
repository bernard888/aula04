"""soma = 0
for x in range(5):
    n1 = int(input("Dgite um valor: "))
    soma += n1
media = soma/5
print(f"a media aritimetica: {media}")"""

#modificação para fazer com que o úsuario atribua o numero de valores a ser pedido

valor = int(input("digite quantos valores vão ser calculados dentro da media: "))
soma = 0
for x in range(valor):
    n1 = int(input("Dgite um valor: "))
    soma += n1
media = soma/valor
print(f"a media aritimetica: {media: .1f}")