'''Task 8 – Data Type Conversion & Rounding
Problem:

Create Series s8 = [1, 2, 3, 4] and convert to float

Create Series s9 = [1.234, 2.345, 3.456] and round to 2 decimals

Output:

Float conversion:
0    1.0
1    2.0
2    3.0
3    4.0
Rounded values:
0    1.23
1    2.35
2    3.46'''

import pandas as pd
s8=pd.Series([1, 2, 3, 4])
print("Float conversion:\n",s8.astype(float))
s9=pd.Series([1.234, 2.345, 3.456])
print("Rounded values:\n",s9.round(2))