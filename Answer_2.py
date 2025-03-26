# Display the last 5 rows and first 5 columns of the dataset.

import pandas as pd

df = pd.read_csv('retail_data.csv')
pd.set_option('display.max_columns', None)
print(df.iloc[-5:, :5])


"""Output:
        Transaction_ID  Customer_ID            Name                     Email  \
293906         4246475        12104    Meagan Ellis      Courtney60@gmail.com   
293907         1197603        69772     Mathew Beck      Jennifer71@gmail.com   
293908         7743242        28449      Daniel Lee  Christopher100@gmail.com   
293909         9301950        45477  Patrick Wilson       Rebecca65@gmail.com   
293910         2882826        53626  Dustin Merritt       William14@gmail.com   

             Phone  
293906  7466353743  
293907  5754304957  
293908  9382530370  
293909  9373222023  
293910  9518926645
"""