num = 0
for x in range(5):
    n1 = int(input("Dgite um valor: "))
    if n1 < 0:
        num += 1
print(f"A quantidade de valores negativos presentes é: {num}")
