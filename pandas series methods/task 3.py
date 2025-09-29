'''Task 3 – Sum, Mean, Min, Max, Median, Std, Variance
Problem:
Create Series s3 = [12, 7, 19, 3, 15]. 
Print sum, mean, min, max, median,
standard deviation, variance (round decimals to 2 places).

Output:

Sum: 56
Mean: 11.2
Min: 3
Max: 19
Median: 12.0
Std: 6.34
Variance: 40.2'''

import pandas as pd
s3=pd.Series([12, 7, 19, 3, 15])
print("Sum:",s3.sum())
print("Mean:",s3.mean())
print("Min: ",s3.min())
print("Max:",s3.max())
print("Median: ",round(s3.median(),2))
print("Std:",round(s3.std(),2))
print("Variance:",round(s3.var(), 2))
