# Display the last 7 rows and last 7 columns.

import pandas as pd

df = pd.read_csv('retail_data.csv')
pd.set_option('display.max_columns', None)
print(df.iloc[-7:, -7:])


"""Output:
       Product_Type   Feedback Shipping_Method Payment_Method Order_Status  \
293904       Tablet    Average        Same-Day           Cash      Pending   
293905       Shorts  Excellent        Standard           Cash    Delivered   
293906      Fiction        Bad        Same-Day           Cash   Processing   
293907       Laptop  Excellent        Same-Day           Cash   Processing   
293908       Jacket    Average         Express           Cash      Shipped   
293909    Furniture       Good        Standard           Cash      Shipped   
293910  Decorations    Average        Same-Day           Cash      Shipped   

        Ratings            products  
293904        2  Amazon Fire Tablet  
293905        4        Chino shorts  
293906        1  Historical fiction  
293907        5             LG Gram  
293908        2               Parka  
293909        4            TV stand  
293910        2              Clocks
"""