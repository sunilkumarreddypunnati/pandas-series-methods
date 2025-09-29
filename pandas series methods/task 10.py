'''Task 10 – Identify Missing Values & Drop NaNs
Problem:
Create Series s11 = [5, None, 10, None, 15].
Print boolean series for .isnull() and .notnull()
Remove NaN values using .dropna()
Output:

Is Null:
0    False
1     True
2    False
3     True
4    False
Not Null:
0     True
1    False
2     True
3    False
4     True
Series after dropping NaN:
0     5
2    10
4    15'''

import pandas as pd
s11=pd.Series([5, None, 10, None, 15])
print("Is Null:\n",s11.isnull())
print("Not Null:\n",s11.notnull())
print("Series after dropping NaN:\n",s11.dropna().astype(int))