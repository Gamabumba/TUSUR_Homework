start_num = input()
our_list = list(start_num)
our_list.insert(3, ",")
our_list.insert(7, ".")
start_num = ''.join(our_list)

print(start_num)