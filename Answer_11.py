# Find orders where the total amount is greater than $1,000, the payment method is "Credit Card," and the product category is "Electronics."

import pandas as pd

df = pd.read_csv('retail_data.csv')
pd.set_option('display.max_columns', None)
print(df.loc[(df['Total_Amount'] > 1000) & (df['Payment_Method'] == 'Credit Card') & (df['Product_Category'] == 'Electronics')].iloc[:, -10:-3])


"""Output:
        Total_Amount Product_Category Product_Brand Product_Type Feedback  \
27       2357.410660      Electronics         Apple       Tablet      Bad   
66       3134.881143      Electronics          Sony   Headphones  Average   
73       1823.483710      Electronics         Apple       Laptop      Bad   
112      3738.363983      Electronics       Samsung   Smartphone      Bad   
132      2959.809090      Electronics       Samsung   Television     Good   
...              ...              ...           ...          ...      ...   
292457   1095.266187      Electronics          Sony   Television      Bad   
292471   1376.736659      Electronics          Sony   Television  Average   
292481   1695.319501      Electronics          Sony   Smartphone     Good   
292486   3723.996697      Electronics       Samsung   Television  Average   
292488   2098.408533      Electronics       Samsung   Television      Bad   

       Shipping_Method Payment_Method  
27            Same-Day    Credit Card  
66            Same-Day    Credit Card  
73            Same-Day    Credit Card  
112           Standard    Credit Card  
132           Standard    Credit Card  
...                ...            ...  
292457        Same-Day    Credit Card  
292471        Same-Day    Credit Card  
292481        Same-Day    Credit Card  
292486        Standard    Credit Card  
292488        Same-Day    Credit Card  

[11807 rows x 7 columns]
"""