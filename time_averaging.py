import pandas as pd
import numpy as np
import math

data = {'name': ['Jason', 'Molly', 'Tina', 'Jake', 'Amy'], 
        'year': [2012, 2012, 2013, 2014, 2014], 
        'reports': [4, 24, 31, 2, 3]}	

df = pd.DataFrame(data)
print(df)

m = df.shape[0]

new_df = pd.DataFrame(columns = df.columns)
# print(new_df)

# print(df.columns)
columns = df.columns

for i in range(len(columns)):
	column = columns[i]
	# print(column)
	col = []
	if column == 'name':
		i = 0
		while i in range(0,m):
			col.append(df.iloc[i][column])
			i += 3
		new_df[column] = col
		continue
	col = []
	i = 0
	while i in range(0,m):
		val1 = df.iloc[i][column]
		if i+1 < m:
			val2 = df.iloc[i+1][column]
		else:
			val2 = 0
		if i+2 < m:	
			val3 = df.iloc[i+2][column]	
		else:
			val3 = 0
		avg = (val1+val2+val3)/3
		col.append(avg)
		i += 3

	# col = np.reshape(col, (len(col),1))
	# print(col)
	new_df[column] = col

print(new_df)