# Display sales records where "Bottle Volume (ml)" is either 500 or 1000, and the "Sale (Dollars)" is over $700.

import pandas as pd

df = pd.read_csv('sample_iowa_liquor_sales.csv')
pd.set_option('display.max_columns', None)
print(df.loc[(df['Bottle Volume (ml)'].isin([500, 1000])) & (df['Sale (Dollars)'] > 700), ['Bottle Volume (ml)', 'Bottles Sold', 'Sale (Dollars)']])


"""Output:
     Bottle Volume (ml)  Bottles Sold  Sale (Dollars)
34                 1000            36          809.28
92                 1000            36          959.40
269                1000            48         1253.76
338                1000            60         2025.00
441                1000           480        15840.00
476                1000            36          999.00
655                1000            36          966.60
773                1000            60          990.00
823                1000            96         1357.44
916                1000            60         1349.40
"""