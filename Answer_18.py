# Show the sales of happened on 10-10-2012 and 11/26/2013 only.

import pandas as pd

df = pd.read_csv('sample_iowa_liquor_sales.csv')
pd.set_option('display.max_columns', None)
print(df.loc[df['Date'].isin(['10-10-2012', '11/26/2013'])])


"""Output:
    Invoice/Item Number        Date  Store Number  \
28         S15983300014  11/26/2013          2551   
269        S15979000005  11/26/2013          3773   
468        S08226100006  10-10-2012          4557   
823        S08161000006  10-10-2012          3621   

                       Store Name          Address          City Zip Code  \
28   Hy-Vee Food Store / Chariton  2001 WEST COURT      CHARITON    50049   
269             Benz Distributing   501 7TH AVE SE  CEDAR RAPIDS    52401   
468        Hometown Foods / Traer    420 SECOND ST         TRAER    50675   
823          Jensen Liquors, Ltd.     615  2ND AVE       SHELDON    51201   

                                        Store Location  County Number  \
28                   2001 WEST COURT\nCHARITON 50049\n             59   
269  501 7TH AVE SE\nCEDAR RAPIDS 52401\n(41.975739...             57   
468  420 SECOND ST\nTRAER 50675\n(42.193386, -92.46...             86   
823  615 2ND AVE\nSHELDON 51201\n(43.18463, -95.854...             71   

      County  Category                     Category Name  Vendor Number  \
28     Lucas   1081600                   WHISKEY LIQUEUR            284   
269     Linn   1011300                TENNESSEE WHISKIES             85   
468     Tama   1081390                 IMPORTED SCHNAPPS            421   
823  O'Brien   1062200  PUERTO RICO & VIRGIN ISLANDS RUM             35   

                             Vendor Name  Item Number  \
28   Charles Jacquin/Independent Spirits        77472   
269             Brown-Forman Corporation        26827   
468                    Sazerac Co., Inc.        69706   
823                 Bacardi U.S.A., Inc.        43127   

                          Item Description  Pack  Bottle Volume (ml)  \
28                           Sweet Revenge     6                 750   
269          Jack Daniels Old #7 Black Lbl    12                1000   
468  Dr. Mcgillicuddy's Root Beer Schnapps    12                 750   
823                   Bacardi Superior Rum    12                1000   

     State Bottle Cost  State Bottle Retail  Bottles Sold  Sale (Dollars)  \
28               10.98                16.47             6           98.82   
269              17.41                26.12            48         1253.76   
468               8.32                12.48             3           37.44   
823               9.43                14.14            96         1357.44   

     Volume Sold (Liters)  Volume Sold (Gallons)  
28                   4.50                   1.19  
269                 48.00                  12.68  
468                  2.25                   0.59  
823                 96.00                  25.36
"""