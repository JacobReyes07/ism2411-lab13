# Disclosure! I used ai in exercise 1 because I got the error ModuleNotFoundError: No module named 'pandas'.
# I was confused because I thought all I needed to do was import pandas as pd but the AI explained that
# I have to install it first.

# Self Assessment 1:
# A boolean filter compares a column against a true or false statement and then outputs only the rows where it was true.
# Self Asssessment 2:
# df['revenue'] is a series and df[['revenue']] is a Data Frame. This distinction matters when using different operations.
# Self Assessment 3:
# Pandas is significantly faster for this task and requires no manual input. This makes it the better option of the two.
def ex(num):
    return print(f"--- Exercise {num} ---")
print()
ex(1)
print()
import pandas as pd
df = pd.read_csv('data/retail_sales.csv')
print(df.head())
print(df.shape)
print(df.columns.tolist())
print(df.dtypes)
print()
ex(2)
print()
south = df[df['region'] == 'South']
print(len(south))
print(south.head())
print()
ex(3)
print()
print(df.sort_values('revenue', ascending=False).head(5))
print()
ex(4)
print()
big_south = df[(df['region']=='South') & (df['revenue']>1000)]
print(len(big_south))
print(big_south.head())
print()
ex(5)
print()
df['per_unit'] = df['revenue'] / df['quantity']
print(df.head())
print(df['per_unit'].mean())
print()
ex(6)
print()
print(df['region'].unique())
print(df['region'].value_counts())
print()
ex(7)
print()
newdf = df[['region', 'product', 'revenue']]
print(newdf)
print()
ex(8)
print()
df.to_csv('data/explored.csv', index=False)
print("Saved")