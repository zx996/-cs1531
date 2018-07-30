integers = [1, 2, 3, 4, 5]
total = 0
integers.append(6)

for i in range(len(integers)):
    total += integers[i]

print(total)
print(sum(integers))
