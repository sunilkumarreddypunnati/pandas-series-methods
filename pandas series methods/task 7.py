'''Task 7 – Reverse Sorting
Problem:
Create Series s7 = [50, 20, 70, 10]. Sort values descending.

Output:

2    70
0    50
1    20
3    10'''

import pandas as pd
s7=pd.Series([50, 20, 70, 10])
print("Sort values descending:\n",s7.sort_values(ascending=False))