# Display the sale records of Polk County but the sale value must be above 500.

import pandas as pd

df = pd.read_csv('sample_iowa_liquor_sales.csv')
pd.set_option('display.max_columns', None)
print(df.loc[(df['County'] == 'Polk') & (df['Sale (Dollars)'] > 500)].iloc[:, 9:-2])


"""Output:
    County  Category                       Category Name  Vendor Number  \
8     Polk   1701100      DECANTERS & SPECIALTY PACKAGES             65   
85    Polk   1062200    PUERTO RICO & VIRGIN ISLANDS RUM             35   
145   Polk   1081305                      APPLE SCHNAPPS             65   
167   Polk   1082900  MISC. IMPORTED CORDIALS & LIQUEURS            330   
338   Polk   1032080                      IMPORTED VODKA             35   
441   Polk   1032080                      IMPORTED VODKA             35   
655   Polk   1011300                  TENNESSEE WHISKIES             85   
668   Polk   1031080                      VODKA 80 PROOF            380   
669   Polk   1081200                      CREAM LIQUEURS            260   

                   Vendor Name  Item Number                Item Description  \
8              Jim Beam Brands          173     Laphroaig w/ Whiskey Stones   
85        Bacardi U.S.A., Inc.        43127            Bacardi Superior Rum   
145            Jim Beam Brands        82607             Dekuyper Sour Apple   
167             Gemini Spirits        66936  Grangala Triple Orange Liqueur   
338       Bacardi U.S.A., Inc.        34422                Grey Goose Vodka   
441       Bacardi U.S.A., Inc.        34422                Grey Goose Vodka   
655   Brown-Forman Corporation        26827   Jack Daniels Old #7 Black Lbl   
668  Phillips Beverage Company        37346                  Phillips Vodka   
669            Diageo Americas        68037   Bailey's Original Irish Cream   

     Pack  Bottle Volume (ml)  State Bottle Cost  State Bottle Retail  \
8      12                 750              19.58                29.37   
85     12                1000               9.43                14.14   
145    12                1000               7.62                11.43   
167    12                 750              10.99                16.49   
338     6                1000              22.50                33.75   
441     6                1000              22.00                33.00   
655    12                1000              17.90                26.85   
668    12                 750               3.57                 5.35   
669    12                1000              17.25                25.88   

     Bottles Sold  Sale (Dollars)  
8              36         1057.32  
85             36          509.04  
145            48          548.64  
167            36          593.64  
338            60         2025.00  
441           480        15840.00  
655            36          966.60  
668           156          834.60  
669            24          621.12
"""