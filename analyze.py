import pandas
import numpy as np
from pandas.tools import plotting

df = pandas.read_csv('test.csv', sep=',', na_values=".")
print(type(df))

numeric_val = []
for row in df['MEDIAN']:
    if row == "A":
        numeric_val.append(4)
    elif row == "A/A-":
        numeric_val.append(3.8)
    elif row == "A-":
        numeric_val.append(3.7)
    elif row == "A-/B+":
        numeric_val.append(3.3)
    elif row == "B+":
        numeric_val.append(3.3)
    elif row == "B":
        numeric_val.append(3)
    elif row == "B-":
        numeric_val.append(2.7)
    elif row == "C+":
        numeric_val.append(2.3)
    elif row == "C":
        numeric_val.append(2)
    elif row == "C-":
        numeric_val.append(1.7)
    elif row == "D":
        numeric_val.append(1)
    elif row == "E":
        numeric_val.append(0)
    else:
        numeric_val.append(-1)

df['NUMERIC'] = numeric_val

dep = []
for row in df['COURSE']:
    dep.append(row[:4])
df['DEPT'] = dep

print(df)
print(df.describe())

by_dept = df.groupby('DEPT')
print(by_dept['NUMERIC'].describe())

by_dept = df.groupby('DEPT').mean().round(3).reset_index()
print(by_dept.sort_values('NUMERIC', ascending=False))
