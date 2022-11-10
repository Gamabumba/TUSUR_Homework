text = input()
text_lits = []

for i in text:
    if i.istitle():
        text_lits.append(i)

print("".join(text_lits))