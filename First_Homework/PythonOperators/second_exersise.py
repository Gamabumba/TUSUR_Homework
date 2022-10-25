import random

first_number, second_number = random.randint(0, 100), random.randint(0, 100)
print("Первое число = ", first_number)
print("Второе число = ", second_number)

print(first_number//second_number, ',', first_number%second_number)