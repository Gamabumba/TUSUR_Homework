text = input()
text_lits = text.split()
count = 0

for i in text_lits:
    if not i.isdigit():
        count += 1
        if count == 3:
            break
    else:
        count = 0

if count == 3:
    print(True)
else:
    print(False)
