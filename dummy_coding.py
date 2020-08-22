import pandas as pd
import numpy as np

data = {'name': ['Jason', 'Molly', 'Tina', 'Jake', 'Amy'], 
        'year': [2012, 2012, 2013, 2014, 2014], 
        'reports': [4, 24, 31, 2, 3]}	

df = pd.DataFrame(data)

print(df)

m = df.shape[0]

unique_names = df.name.unique()
# print(unique_names)

for name in unique_names:
	col = []
	for index, row in df.iterrows():
		# print(row['name'])
		if row['name'] == name:
			col.append('1')
		else:
			col.append('0')
	# col = np.reshape(col, (m,1))
	df[name] = col			

df = df.drop(['name'], axis=1)

print(df)