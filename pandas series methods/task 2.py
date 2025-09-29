'''Task 2 – Values, Index, dtype, shape
Problem:
Using Series s2 = [1, 2, 3, 4, 5] 
with index ['A','B','C','D','E'], 
print:

.values

.index

.dtype

.shape

Output:

Values: [1 2 3 4 5]
Index: Index(['A','B','C','D','E'], dtype='object')
Dtype: int64
Shape: (5,)'''

import pandas as pd
s2=pd.Series([1, 2, 3, 4, 5],index=['A','B','C','D','E'])
print("Values:",s2.values)
print("Index:",s2.index)
print("Dtype:",s2.dtype)
print("Shape:",s2.shape)

