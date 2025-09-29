'''Task 6 – Sort by Values & Index
Problem:
Create Series s6 = [300, 100, 200] with index ['x','y','z'].

Sort by values ascending

Sort by index ascending

Output:

Sorted by values:
y    100
z    200
x    300
Sorted by index:
x    300
y    100
z    200'''

import pandas as pd
s6=pd.Series([300, 100, 200],index=['x','y','z'])
print("Sorted by values:\n",s6.sort_values())
print("Sorted by index:\n",s6.sort_index())
print("Rank:\n",s6.rank())