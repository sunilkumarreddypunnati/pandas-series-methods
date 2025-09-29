'''Task 11 – Full Pipeline
Problem:
Create Series s12 = [5, 10, 10, None, 20, 5, 30, None]. 
Perform:
Print first 5 elements
Identify NaN values
Remove NaN and duplicates
Sort ascending
Print sum, mean, min, max
Print unique values and frequency
'''
import pandas as pd
# Create Series
s12 = pd.Series([5, 10, 10, None, 20, 5, 30, None])
# 1. First 5 elements
print("First 5 elements:\n", s12.head(5))
# 2. Identify NaN values
print("NaN Check:\n", s12.isnull())
# 3. Remove NaN and duplicates
cleaned_s12 = s12.dropna().drop_duplicates()
print("Cleaned Series (No NaN, No Duplicates):\n", cleaned_s12)
# 4. Sort ascending
sorted_s12 = cleaned_s12.sort_values()
print("Sorted Series:\n", sorted_s12)
# 5. Sum, Mean, Min, Max
print("Sum:", sorted_s12.sum())
print("Mean:", sorted_s12.mean())
print("Min:", sorted_s12.min())
print("Max:", sorted_s12.max())
# 6. Unique values
print("Unique Values:", sorted_s12.unique())
# 7. Frequency of each value
print("Frequency:\n", sorted_s12.value_counts())
