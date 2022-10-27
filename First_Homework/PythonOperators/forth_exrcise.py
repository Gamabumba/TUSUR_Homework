start_num = input("Введите целое число: ")
num_list = list(start_num)
if num_list[0] == "-":
    num_list.pop(0)
    num_list.reverse()
    num_list.insert(0, '-')
else:
    num_list.reverse()

final_num = "".join(num_list)
print('"Обратное" ему число:', final_num)