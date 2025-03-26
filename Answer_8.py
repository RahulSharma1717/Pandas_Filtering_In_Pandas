# Display the data of Germany where ratings are between 3-5(inclusive).

import pandas as pd

df = pd.read_csv('retail_data.csv')
pd.set_option('display.max_columns', None)
print(df.loc[(df['Country'] == 'Germany') & ((df['Ratings'] >= 3) & (df['Ratings'] <= 5))].iloc[:, list(range(9, 13)) + list(range(26, 30))])


"""Output:
        Country  Age  Gender  Income Payment_Method Order_Status  Ratings  \
0       Germany   21    Male     Low     Debit Card      Shipped        5   
9       Germany   25    Male  Medium           Cash    Delivered        4   
17382   Germany   19  Female  Medium         PayPal    Delivered        4   
17390   Germany   19    Male  Medium     Debit Card    Delivered        5   
17394   Germany   19    Male  Medium    Credit Card    Delivered        3   
...         ...  ...     ...     ...            ...          ...      ...   
293873  Germany   47    Male  Medium           Cash      Shipped        3   
293890  Germany   27    Male     Low           Cash      Shipped        4   
293896  Germany   18  Female  Medium           Cash      Shipped        5   
293897  Germany   30  Female    High           Cash   Processing        4   
293907  Germany   35  Female     Low           Cash   Processing        5   

                   products  
0            Cycling shorts  
9                   Candles  
17382                 Drill  
17390        Flavored water  
17394            Towel rack  
...                     ...  
293873    In-ear headphones  
293890  Fit and flare dress  
293896         Orange juice  
293897       Scoop neck tee  
293907              LG Gram  

[33888 rows x 8 columns]
"""