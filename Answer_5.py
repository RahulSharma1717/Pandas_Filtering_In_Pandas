# Display the rows where the order status is shipped.

import pandas as pd

df = pd.read_csv('retail_data.csv')
pd.set_option('display.max_columns', None)
print(df.loc[df['Order_Status'] == 'Shipped'].iloc[:, -5:])


"""Output:
       Shipping_Method Payment_Method Order_Status  Ratings           products
0             Same-Day     Debit Card      Shipped        5     Cycling shorts
4             Standard           Cash      Shipped        1  Chocolate cookies
10            Standard    Credit Card      Shipped        2    Screwdriver set
14            Same-Day           Cash      Shipped        1         V-neck tee
16            Same-Day     Debit Card      Shipped        2     Flavored water
...                ...            ...          ...      ...                ...
293899         Express           Cash      Shipped        3            Puzzles
293900        Same-Day           Cash      Shipped        5               iPad
293908         Express           Cash      Shipped        2              Parka
293909        Standard           Cash      Shipped        4           TV stand
293910        Same-Day           Cash      Shipped        2             Clocks

[63275 rows x 5 columns]
"""