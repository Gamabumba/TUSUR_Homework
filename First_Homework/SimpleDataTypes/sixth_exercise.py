value = input()
res = 1
count = 0
for i in value:
    if i == '0':
        pass
    else:
        res *= int(i)
        count += 1

if count == 0:
    res = 0

print(res)
