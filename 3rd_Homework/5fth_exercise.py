text = "привет мир!"
f_text = []

for i in range(len(text)):
    if i >= 3 and i <= 8:
        f_text.append(text[i].upper())
    else:
        f_text.append(text[i])

print(''.join(f_text))
