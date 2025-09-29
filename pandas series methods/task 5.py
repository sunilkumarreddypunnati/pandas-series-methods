'''Task 5 – Identify & Remove Duplicates
Problem:
Create Series s5 = [5, 10, 5, 15, 20, 10].

Print boolean series for duplicates

Print series after removing duplicates

Output:

Duplicates:
0    False
1    False
2     True
3    False
4    False
5     True
Series after removing duplicates:
0     5
1    10
3    15
4    20'''

import pandas as pd
s5=pd.Series([5, 10, 5, 15, 20, 10])
print("Duplicates:\n",s5.duplicated())
print("Series after removing duplicates:\n",s5.drop_duplicates())