s = "нет такого месяца"
months = {12: "Зима", 1: "Зима", 2: "Зима", 3: "Весна", 4: "Весна", 5: "Весна", 6: "Лето", 7: "Лето", 8: "Лето",
          9: "Осень", 10: "Осень", 11: "Осень"}

def season(month):
    global s
    if month in months:
        s = months[month]
    print(s)

month = int(input())
season(month)
