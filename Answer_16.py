# Find out the sales in Linn county but the bottle volume must be more than 1000ml.

import pandas as pd

df = pd.read_csv('sample_iowa_liquor_sales.csv')
pd.set_option('display.max_columns', None)
print(df.loc[(df['County'] == 'Linn') & (df['Bottle Volume (ml)'] > 1000), ['County', 'Bottle Volume (ml)', 'Sale (Dollars)']])


"""Output:
    County  Bottle Volume (ml)  Sale (Dollars)
74    Linn                1750          116.88
221   Linn                3000           44.58
244   Linn                1750          176.16
348   Linn                1750           73.74
406   Linn                1750           20.76
533   Linn                1750           90.00
546   Linn                1750           17.74
547   Linn                1750           98.94
597   Linn                1200           54.00
637   Linn                1750           64.02
694   Linn                1750          498.48
732   Linn                1750          101.58
755   Linn                1750           63.72
782   Linn                1750          128.40
841   Linn                1750          192.60
872   Linn                1750          260.88
886   Linn                1750           67.14
"""

