# Retrieve the first 3 rows

import pandas as pd

df = pd.read_csv('retail_data.csv')
pd.set_option('display.max_columns', None)
print(df.iloc[:3, ])


"""Output:
   Transaction_ID  Customer_ID                 Name              Email  \
0         8691788        37249  Michelle Harrington  Ebony39@gmail.com   
1         2174773        69749          Kelsey Hill   Mark36@gmail.com   
2         6679610        30192         Scott Jensen  Shane85@gmail.com   

        Phone             Address        City            State  Zipcode  \
0  1414786801   3959 Amanda Burgs    Dortmund           Berlin    77985   
1  6852899987  82072 Dawn Centers  Nottingham          England    99071   
2  8362160449   4133 Young Canyon     Geelong  New South Wales    75929   

     Country  Age  Gender Income Customer_Segment        Date  Year  \
0    Germany   21    Male    Low          Regular   9/18/2023  2023   
1         UK   19  Female    Low          Premium  12/31/2023  2023   
2  Australia   48    Male    Low          Regular   4/26/2023  2023   

       Month      Time  Total_Purchases      Amount  Total_Amount  \
0  September  22:03:55                3  108.028757    324.086270   
1   December  08:42:04                2  403.353907    806.707815   
2      April  04:06:29                3  354.477600   1063.432799   

  Product_Category  Product_Brand Product_Type   Feedback Shipping_Method  \
0         Clothing           Nike       Shorts  Excellent        Same-Day   
1      Electronics        Samsung       Tablet  Excellent        Standard   
2            Books  Penguin Books   Children's    Average        Same-Day   

  Payment_Method Order_Status  Ratings          products  
0     Debit Card      Shipped        5    Cycling shorts  
1    Credit Card   Processing        4        Lenovo Tab  
2    Credit Card   Processing        2  Sports equipment
"""