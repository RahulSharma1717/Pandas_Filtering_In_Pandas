# Display the first 10 rows of the last 10 columns.

import pandas as pd

df = pd.read_csv('sample_iowa_liquor_sales.csv')
pd.set_option('display.max_columns', None)
print(df.iloc[:10, -10:])


"""Output:
   Item Number              Item Description  Pack  Bottle Volume (ml)  \
0          238  Forbidden Secret Coffee Pack     6                1500   
1          173   Laphroaig w/ Whiskey Stones    12                 750   
2          238  Forbidden Secret Coffee Pack     6                1500   
3          258           Rumchata "GoChatas"     1                6000   
4          238  Forbidden Secret Coffee Pack     6                1500   
5          238  Forbidden Secret Coffee Pack     6                1500   
6          238  Forbidden Secret Coffee Pack     6                1500   
7          238  Forbidden Secret Coffee Pack     6                1500   
8          173   Laphroaig w/ Whiskey Stones    12                 750   
9          238  Forbidden Secret Coffee Pack     6                1500   

   State Bottle Cost  State Bottle Retail  Bottles Sold  Sale (Dollars)  \
0              11.62                17.43             6          104.58   
1              19.58                29.37             4          117.48   
2              11.62                17.43             1           17.43   
3              99.00               148.50             1          148.50   
4              11.62                17.43             6          104.58   
5              11.62                17.43             3           52.29   
6              11.62                17.43             6          104.58   
7              11.62                17.43             2           34.86   
8              19.58                29.37            36         1057.32   
9              11.62                17.43            12          209.16   

   Volume Sold (Liters)  Volume Sold (Gallons)  
0                   9.0                   2.38  
1                   3.0                   0.79  
2                   1.5                   0.40  
3                   6.0                   1.59  
4                   9.0                   2.38  
5                   4.5                   1.19  
6                   9.0                   2.38  
7                   3.0                   0.79  
8                  27.0                   7.13  
9                  18.0                   4.76
"""