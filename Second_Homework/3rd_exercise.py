n = int(input())
n_list = []

if n not in range(10) or n == 0:
    print("Введите число от 1 до 9")

while n != 0:
    n_list.append(n)
    n -= 1

out_list = list(reversed(n_list))
print("".join(map(str,out_list)))
