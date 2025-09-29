'''Task 1 – Head & Tail
Problem:
Create a Series s1 = [5, 10, 15, 20, 25] 
with index ['a','b','c','d','e'].

Print the first 3 elements using .head()

Print the last 2 elements using .tail()

Output:

First 3 elements:
a     5
b    10
c    15
Last 2 elements:
d    20
e    25'''

import pandas as pd
s1=pd.Series([5, 10, 15, 20, 25],index=['a','b','c','d','e'])
print("First 3 elements:\n",s1.head(3))
print("Last 2 elements:\n",s1.tail(2))