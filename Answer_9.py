# Display the data of Adidas and Nike with excellent feedback.

import pandas as pd

df = pd.read_csv('retail_data.csv')
pd.set_option('display.max_columns', None)
print(df.loc[(df['Product_Brand'].isin(['Adidas', 'Nike'])) & (df['Feedback'] == 'Excellent')].iloc[:, -8:-5])


"""Output:
       Product_Brand Product_Type   Feedback
0               Nike       Shorts  Excellent
39            Adidas        Shoes  Excellent
84            Adidas       Jacket  Excellent
140           Adidas       Jacket  Excellent
150           Adidas       Jacket  Excellent
...              ...          ...        ...
293731          Nike       Shorts  Excellent
293745          Nike        Shoes  Excellent
293809        Adidas      T-shirt  Excellent
293897        Adidas      T-shirt  Excellent
293905          Nike       Shorts  Excellent

[12466 rows x 3 columns]
"""