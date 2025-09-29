'''Task 9 – Apply Custom Function
Problem:
Create Series s10 = [2, 4, 6, 8] and 
multiply each value by 10 using .apply().

Output:

0    20
1    40
2    60
3    80'''

import pandas as pd
s10=pd.Series([2, 4, 6, 8])
print(s10.apply(lambda s10:s10*10))