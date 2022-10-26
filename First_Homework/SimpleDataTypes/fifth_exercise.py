height = int(input())
width = height * 3

for i in range(height):
    print(('.|.' * i).center(width, '-'))

print('WELCOME'.center(width, '-'))

for i in reversed(range(height)):
    print(('.|.' * i).center(width, '-'))