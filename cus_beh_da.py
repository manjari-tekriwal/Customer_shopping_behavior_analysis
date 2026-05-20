import pandas as pd
df = pd.read_csv("C:/Users/HP/Downloads/customer_shopping_behavior.csv")
print(df.head())
df.info()
df.describe(include = "all")