# Create a sample of 50 rows from the above dataset.

import pandas as pd

df = pd.read_csv('sample_iowa_liquor_sales.csv')
pd.set_option('display.max_columns', None)
sample_df = df.sample(50)
print(sample_df.iloc[list(range(0, 10)) + list(range(40, 50)), :])    # Printing the first 10 and last 10 rows of sample dataset


"""Output:
    Invoice/Item Number        Date  Store Number  \
29         S06855800032  07/31/2012          2522   
408        S15145100080  10/15/2013          2620   
20         S23647700049  01/26/2015          4742   
231        S18058600013  03/25/2014          3830   
116        S24742300137  03/26/2015          5102   
682        S28796200019  11-02-2015          2653   
43         S16168900009  12-09-2013          4110   
435        S19624400020  06/18/2014          3715   
820        S22412300064  11/17/2014          3838   
440        S07661400013  09-11-2012          3963   
776        S28016900028  09/21/2015          2628   
377        S04785200022  03/28/2012          3762   
571        S27369100002  08/17/2015          2633   
800        S21164400042  09-11-2014          2550   
110        S20329100034  07/31/2014          3698   
856        S23503500019  01/14/2015          2512   
218        S09706900021  12/26/2012          2510   
784        S12191800002  05/14/2013          3959   
444        S04944000001  04-09-2012          4581   
394        S10667000018  02/18/2013          2500   

                               Store Name               Address  \
29   Hy-Vee Wine and Spirits / Spirit Lak            HWY 9 & 71   
408              Hy-Vee / Windsor Heights   7101 UNIVERSITY AVE   
20   No Frills Supermarkets #786 / Counci      1817, W BROADWAY   
231               Wal-Mart 1435 / Creston         806 LAUREL ST   
116                        Wilkie Liquors      724, 1st  ST  SE   
682  Hy-Vee Wine and Spirits / Washington     1004 W MADISON ST   
43                  Brothers Market, Inc.        706 HIGHWAY 57   
435             Kimberly Mart / Davenport    1714 E KIMBERLY RD   
820                 Schnucks / Bettendorf         858 MIDDLE RD   
440      Tobacco Hut #14 / Council Bluffs       1925 W BROADWAY   
776            Hy-Vee Food Store / Eldora        1616 EDGINGTON   
377              Wine and Spirits Gallery       7690 HICKMAN RD   
571          Hy-Vee #3 / BDI / Des Moines       3221 SE 14TH ST   
800           Hy-Vee Food Store / Osceola       510 WEST MCLANE   
110              Ingersoll Wine Merchants         1300  50TH ST   
856   Hy-Vee Wine and Spirits / Iowa City    1720 WATERFRONT DR   
218    Hy-Vee Drugstore #3 / Cedar Rapids  2405 MT VERNON RD SE   
784   Hartig Drug Company #8 / University   1600 UNIVERSITY AVE   
444              Prime Mart / Cedar Falls        2728 CENTER ST   
394           Hy-Vee Food Store #1 / Ames    3800 W LINCOLN WAY   

                City Zip Code  \
29       SPIRIT LAKE    51360   
408  WINDSOR HEIGHTS    50311   
20    COUNCIL BLUFFS    51501   
231          CRESTON    50801   
116     MOUNT VERNON    52314   
682       WASHINGTON    52353   
43       PARKERSBURG    50665   
435        DAVENPORT    52807   
820       BETTENDORF    52722   
440   COUNCIL BLUFFS    51501   
776           ELDORA    50627   
377  WINDSOR HEIGHTS    50322   
571       DES MOINES    50320   
800          OSCEOLA    50213   
110  WEST DES MOINES    50266   
856        IOWA CITY    52240   
218     CEDAR RAPIDS    52403   
784          DUBUQUE    52001   
444      CEDAR FALLS    50613   
394             AMES    50010   

                                        Store Location  County Number  \
29                 HWY 9 &amp; 71\nSPIRIT LAKE 51360\n             30   
408  7101 UNIVERSITY AVE\nWINDSOR HEIGHTS 50311\n(4...             77   
20   1817, W BROADWAY\nCOUNCIL BLUFFS 51501\n(41.26...             78   
231  806 LAUREL ST\nCRESTON 50801\n(41.047716, -94....             88   
116  724, 1st ST SE\nMOUNT VERNON 52314\n(41.91776,...             57   
682  1004 W MADISON ST\nWASHINGTON 52353\n(41.29657...             92   
43   706 HIGHWAY 57\nPARKERSBURG 50665\n(42.570361,...             12   
435  1714 E KIMBERLY RD\nDAVENPORT 52807\n(41.55696...             82   
820  858 MIDDLE RD\nBETTENDORF 52722\n(41.539421, -...             48   
440  1925 W BROADWAY\nCOUNCIL BLUFFS 51501\n(41.261...             78   
776  1616 EDGINGTON\nELDORA 50627\n(42.360633, -93....             42   
377  7690 HICKMAN RD\nWINDSOR HEIGHTS 50322\n(41.61...             77   
571  3221 SE 14TH ST\nDES MOINES 50320\n(41.554101,...             77   
800  510 WEST MCLANE\nOSCEOLA 50213\n(41.030575, -9...             20   
110  1300 50TH ST\nWEST DES MOINES 50266\n(41.59085...             77   
856  1720 WATERFRONT DR\nIOWA CITY 52240\n(41.64277...             52   
218  2405 MT VERNON RD SE\nCEDAR RAPIDS 52403\n(41....             57   
784  1600 UNIVERSITY AVE\nDUBUQUE 52001\n(42.498324...             31   
444  2728 CENTER ST\nCEDAR FALLS 50613\n(42.561054,...              7   
394  3800 W LINCOLN WAY\nAMES 50010\n(42.023145, -9...             85   

            County  Category                       Category Name  \
29       Dickinson   1062200    PUERTO RICO & VIRGIN ISLANDS RUM   
408           Polk   1081317                      GRAPE SCHNAPPS   
20   Pottawattamie   1062200    PUERTO RICO & VIRGIN ISLANDS RUM   
231          Union   1081200                      CREAM LIQUEURS   
116           Linn   1042100                   IMPORTED DRY GINS   
682     Washington   1051010             AMERICAN GRAPE BRANDIES   
43          Butler   1062310                          SPICED RUM   
435          Scott   1032080                      IMPORTED VODKA   
820           Iowa   1062200    PUERTO RICO & VIRGIN ISLANDS RUM   
440  Pottawattamie   1031100                     100 PROOF VODKA   
776         Hardin   1081315                   CINNAMON SCHNAPPS   
377           Polk   1052010             IMPORTED GRAPE BRANDIES   
571           Polk   1012100                   CANADIAN WHISKIES   
800         Clarke   1081330                      PEACH SCHNAPPS   
110           Polk   1032200               IMPORTED VODKA - MISC   
856        Johnson   1062310                          SPICED RUM   
218           Linn   1081900  MISC. AMERICAN CORDIALS & LIQUEURS   
784        Dubuque   1062200    PUERTO RICO & VIRGIN ISLANDS RUM   
444     Black Hawk   1081600                     WHISKEY LIQUEUR   
394          Story   1081390                   IMPORTED SCHNAPPS   

     Vendor Number                       Vendor Name  Item Number  \
29              35              Bacardi U.S.A., Inc.        43125   
408             65                   Jim Beam Brands        82636   
20              35              Bacardi U.S.A., Inc.        43128   
231            461                     Campari(skyy)        68126   
116            260                   Diageo Americas        28890   
682            259                Heaven Hill Brands        52316   
43             260                   Diageo Americas        43338   
435            370  Pernod Ricard USA/Austin Nichols        34003   
820            434                    Luxco-St Louis        45278   
440            300      Mccormick Distilling Company        36886   
776             65                   Jim Beam Brands        82611   
377            420           Moet Hennessy USA, Inc.        48154   
571            260                   Diageo Americas        10836   
800            434                    Luxco-St Louis        84456   
110             35              Bacardi U.S.A., Inc.        34605   
856            260                   Diageo Americas        43285   
218            322   Prestige Wine and Spirits Group        75208   
784            434                    Luxco-St Louis        45248   
444             85          Brown-Forman Corporation        86886   
394            421                 Sazerac Co., Inc.        69611   

                           Item Description  Pack  Bottle Volume (ml)  \
29                 Bacardi Superior Rum Pet    12                 750   
408          Dekuyper Grape Pucker Schnapps    12                 750   
20                     Bacardi Superior Rum     6                1750   
231           Carolan's Irish Cream Liqueur    12                 750   
116                   Tanqueray Rangpur Gin    12                 750   
682                   Christian Bros Brandy    12                 750   
43                Captain Morgan Spiced Rum     6                1750   
435            Absolut Swedish Vodka 80 Prf    24                 200   
820                     Paramount White Rum     6                1750   
440                         Mccormick Vodka    12                 750   
776                      Dekuyper Hot Damn!    12                 750   
377                          Hennessy Black    12                 375   
571                       Crown Royal Black    12                 750   
800                Paramount Peach Schnapps    12                 750   
110               Grey Goose La Poire Vodka     6                 750   
856  Captain Morgan Original Spiced Rum Pet    12                 750   
218                      Kinky Liqueur Mini     6                 500   
784                      Paramount Gold Rum     6                1750   
444                        Southern Comfort    12                 750   
394   Dr. Mcgillicuddy's Apple Pie Schnapps    12                 750   

     State Bottle Cost  State Bottle Retail  Bottles Sold  Sale (Dollars)  \
29                7.53                11.30            12          135.60   
408               5.30                 8.45             4           33.80   
20               15.00                22.50            12          270.00   
231               7.70                11.55            24          277.20   
116              12.50                18.75             3           56.25   
682               5.92                 8.88             3           26.64   
43               17.75                26.62             6          159.72   
435               3.99                 5.99            24          143.76   
820               7.84                11.76             6           70.56   
440               3.30                 4.96             5           24.80   
776               6.30                 9.45             2           18.90   
377              11.49                17.24             1           17.24   
571              17.00                25.50             1           25.50   
800               4.09                 6.14             5           30.70   
110              18.49                27.74             2           55.48   
856               9.00                13.50            12          162.00   
218               4.67                 7.00             6           42.00   
784               7.58                11.37             6           68.22   
444               9.36                14.04            12          168.48   
394               8.32                12.48            12          149.76   

     Volume Sold (Liters)  Volume Sold (Gallons)  
29                   9.00                   2.38  
408                  3.00                   0.79  
20                  21.00                   5.55  
231                 18.00                   4.76  
116                  2.25                   0.59  
682                  2.25                   0.59  
43                  10.50                   2.77  
435                  4.80                   1.27  
820                 10.50                   2.77  
440                  3.75                   0.99  
776                  1.50                   0.40  
377                  0.38                   0.10  
571                  0.75                   0.20  
800                  3.75                   0.99  
110                  1.50                   0.40  
856                  9.00                   2.38  
218                  3.00                   0.79  
784                 10.50                   2.77  
444                  9.00                   2.38  
394                  9.00                   2.38
"""
