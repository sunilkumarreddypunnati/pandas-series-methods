'''Task 4 – Unique Values & Frequency
Problem:
Create Series s4 = [10, 20, 10, 30, 20, 40].

Print unique values

Print number of unique values

Print frequency of each value

Output:

Unique values: [10 20 30 40]
Number of unique values: 4
Frequency:
10    2
20    2
30    1
40    1'''

import pandas as pd
s4=pd.Series([10, 20, 10, 30, 20, 40])
print("Unique values:",s4.unique())
print("Number of unique values:",s4.nunique())
print("Unique values:\n",s4.value_counts())