# Find the companies that have excellent feedback for electronics in the American market.

import pandas as pd

df = pd.read_csv('retail_data.csv')
pd.set_option('display.max_columns', None)
new_df = df.loc[(df['Feedback'] == 'Excellent') & (df['Product_Category'] == 'Electronics') & (df['Country'] == 'USA')]
print(new_df[['Feedback', 'Product_Category', 'Country']])


"""Output:
         Feedback Product_Category Country
17556   Excellent      Electronics     USA
17575   Excellent      Electronics     USA
17577   Excellent      Electronics     USA
17578   Excellent      Electronics     USA
17584   Excellent      Electronics     USA
...           ...              ...     ...
293485  Excellent      Electronics     USA
293634  Excellent      Electronics     USA
293754  Excellent      Electronics     USA
293762  Excellent      Electronics     USA
293900  Excellent      Electronics     USA

[5881 rows x 3 columns]
"""