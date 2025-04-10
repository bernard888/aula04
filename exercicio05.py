"""num = 0
num2 = 0
for x in range(5):
    n1 = int(input("Dgite um valor: "))
    if n1 >= 10 and n1 <= 20:
        num += 1
    else:
        num2 += 1
print(f"A quantidade de valores entre 10 e 20 presentes é de: {num}"
      f"\nA quantidade de valores fora do intervalo de 10 e 20 é: {num2}")"""

#codigo mais eficiente

num = 0
num2 = 0
for x in range(5):
    n1 = int(input("Dgite um valor: "))
    if n1 < 10 or n1 > 20:
        num += 1
num2 = 5-n1
print(f"A quantidade de valores entre 10 e 20 presentes é de: {num}"
      f"\nA quantidade de valores fora do intervalo de 10 e 20 é: {num2}")