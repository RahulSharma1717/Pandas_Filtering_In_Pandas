# Display orders shipped to Canada with a rating of 3 or higher.

import pandas as pd

df = pd.read_csv('retail_data.csv')
pd.set_option('display.max_columns', None)
print(df.loc[(df['Country'] == 'Canada') & (df['Ratings'] >= 3)].iloc[:, list(range(9, 13)) + list(range(26, 30))])


"""Output:
       Country  Age  Gender  Income Payment_Method Order_Status  Ratings  \
3       Canada   56    Male    High         PayPal   Processing        4   
17383   Canada   19    Male  Medium    Credit Card    Delivered        5   
17397   Canada   19    Male  Medium           Cash    Delivered        3   
17398   Canada   19    Male  Medium         PayPal    Delivered        3   
17409   Canada   19  Female  Medium     Debit Card    Delivered        4   
...        ...  ...     ...     ...            ...          ...      ...   
293868  Canada   69  Female    High           Cash   Processing        4   
293893  Canada   19    Male    High           Cash   Processing        4   
293899  Canada   39  Female    High           Cash      Shipped        3   
293903  Canada   63    Male     Low           Cash      Pending        5   
293909  Canada   41    Male  Medium           Cash      Shipped        4   

             products  
3       Utility knife  
17383        Sundress  
17397     Windbreaker  
17398         Blanket  
17409     Mango juice  
...               ...  
293868      Xiaomi Mi  
293893      Dystopian  
293899        Puzzles  
293903          Level  
293909       TV stand  

[30163 rows x 8 columns]
"""