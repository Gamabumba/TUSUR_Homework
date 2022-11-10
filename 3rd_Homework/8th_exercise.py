def more_than_five(lst):
    final_lst = []
    for i in lst:
        if abs(i) > 10:
            final_lst.append(i)
    return final_lst

lst = [-1, -11, 28, 17, 0, 6]
print(more_than_five(lst))
