# Display the data for the electronics and clothing category only.

import pandas as pd

df = pd.read_csv('retail_data.csv')
pd.set_option('display.max_columns', None)
print(df.loc[(df['Product_Category'] == 'Clothing') | (df['Product_Category'] == 'Electronics')].iloc[:, -9:])


"""Output:
       Product_Category Product_Brand Product_Type   Feedback Shipping_Method  \
0              Clothing          Nike       Shorts  Excellent        Same-Day   
1           Electronics       Samsung       Tablet  Excellent        Standard   
5           Electronics         Apple       Tablet       Good         Express   
6           Electronics       Samsung   Television        Bad        Standard   
7              Clothing          Zara        Shirt        Bad        Same-Day   
...                 ...           ...          ...        ...             ...   
293900      Electronics       Samsung       Tablet  Excellent        Same-Day   
293904      Electronics         Apple       Tablet    Average        Same-Day   
293905         Clothing          Nike       Shorts  Excellent        Standard   
293907      Electronics         Apple       Laptop  Excellent        Same-Day   
293908         Clothing        Adidas       Jacket    Average         Express   

       Payment_Method Order_Status  Ratings            products  
0          Debit Card      Shipped        5      Cycling shorts  
1         Credit Card   Processing        4          Lenovo Tab  
5              PayPal      Pending        4          Lenovo Tab  
6                Cash   Processing        1             QLED TV  
7                Cash   Processing        1         Dress shirt  
...               ...          ...      ...                 ...  
293900           Cash      Shipped        5                iPad  
293904           Cash      Pending        2  Amazon Fire Tablet  
293905           Cash    Delivered        4        Chino shorts  
293907           Cash   Processing        5             LG Gram  
293908           Cash      Shipped        2               Parka  

[122647 rows x 9 columns]
"""