x = int(input())

if x % 2 != 0:
    print("Плохо")
elif x == 4 or x == 2:
    print("Неплохо")
elif x > 5 and x < 21:
    print("Так себе")
else:
    print("Отлично")
