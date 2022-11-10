x=int(input('введите число 0-1000: '))
if x in range (1001):
    if x % 2==0 or x % 3==0 or x % 5==0:
        print('число не простое ')
    else:
        print('простое число ')
else:
    print('число вне диапозона')
