# Display the data of Berlin state.

import pandas as pd

df = pd.read_csv('retail_data.csv')
pd.set_option('display.max_columns', None)
print(df.loc[df['State'] == 'Berlin'].iloc[:, :8])


"""Output:
        Transaction_ID  Customer_ID                 Name  \
0              8691788        37249  Michelle Harrington   
7              2344675        26603        Angela Fields   
9              4926148        31878            Lori Bell   
17382          3680043        78484    Mr. Zachary Marks   
17390          5206426        66989    Angel Fitzpatrick   
...                ...          ...                  ...   
293884         7666480        29139            Jane Ball   
293890         1554068        72401       Matthew Miller   
293896         5346939        12465        Daniel Miller   
293897         5781099        41133       Cheryl Collins   
293907         1197603        69772          Mathew Beck   

                       Email       Phone                       Address  \
0          Ebony39@gmail.com  1414786801             3959 Amanda Burgs   
7          Tanya94@gmail.com  3668096144               237 Young Curve   
9        Jessica33@gmail.com  6004895059            6225 William Lodge   
17382       Tyler6@gmail.com  2831499082            085 Nguyen Highway   
17390       Evan31@gmail.com  7490023454             548 Gonzalez Camp   
...                      ...         ...                           ...   
293884       Amy55@gmail.com  8579604153            57855 Julie Divide   
293890    Ashley11@gmail.com  7507492899             8471 Dana Station   
293896   Kaitlin85@gmail.com  8981601821                235 Reed Glens   
293897      Tina76@gmail.com  6851286333  6806 Buchanan Place Apt. 569   
293907  Jennifer71@gmail.com  5754304957             52809 Mark Forges   

             City   State  
0        Dortmund  Berlin  
7          Munich  Berlin  
9         Cologne  Berlin  
17382     Cologne  Berlin  
17390     Leipzig  Berlin  
...           ...     ...  
293884       Bonn  Berlin  
293890  Bielefeld  Berlin  
293896     Bochum  Berlin  
293897  Nuremberg  Berlin  
293907    Hanover  Berlin  

[51433 rows x 8 columns]
"""