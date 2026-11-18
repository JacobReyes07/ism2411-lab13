# Disclosure! I used ai in exercise 1 because I got the error ModuleNotFoundError: No module named 'pandas'.
# I was confused because I thought all I needed to do was import pandas as pd but the AI explained that
# I have to install it first.

def ex(num):
    return print(f"--- Exercise {num} ---")

ex(1)

import pandas as pd

df = pd.read_csv('data/retail_sales.csv')
print(df.head())
print(df.shape)
print(df.columns.tolist())
print(df.dtypes)

ex(2)

south = df[df['region'] == 'South']
print(len(south))
print(south.head())

ex(3)

print(df.sort_values('revenue', ascending=False).head(5))

ex(4)

big_south = df[(df['region']=='South') & (df['revenue']>1000)]
print(len(big_south))
print(big_south.head())

ex(5)

df['per_unit'] = df['revenue'] / df['quantity']
print(df.head())