mass = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for i in range(1, int(len(mass) / 2), 2):
    if not len(mass) % 2:
        mass[i], mass[-i] = mass[-i], l[i]
    else:
        mass[i], mass[-i - 1] = mass[-i - 1], mass[i]

print(mass)
