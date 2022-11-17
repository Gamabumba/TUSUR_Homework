import pandas as pd
import random

d = [{"Name": "Виктор", "Age": 18},
 {"Name": "Мария", "Age": 21},
 {"Name": "Иван", "Age": 19},
 {"Name": "Иван", "Age": 25},
 {"Name": "Алексей", "Age": 20}]

df = pd.DataFrame(d)

num_list=[]
while len(num_list)<5:
    num=str(random.randint(0,999999999)).zfill(9)
    if not num in num_list:
        num_list.append(num)

df['phone_number'] = num_list

print(df)