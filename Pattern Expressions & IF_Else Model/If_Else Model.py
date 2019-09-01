import pandas
import re

# to read data from a csv file
from qtconsole import styles

df = pandas.read_csv(r"Book111.csv")
df.head()
type(df)
df.shape
df["H.Name"]
df.style.format("{:<20}")
while True:
	User = str()
	User = input("\n\nEnter Blood Group You Want ")

	if User == 'A+':
		print(df[["Review1","H.Name"]][(df["A+"] > 15) & (df["Review1"] >= 3) & (df["Review2"] >= 3)])

	elif User =='B+':
		print(df[["Review1","H.Name"]][(df["B+"] > 15) & (df["Review1"] >= 3) & (df["Review2"] >= 3)])

	elif User == 'AB+':
		print(df[["Review1","H.Name"]][(df["AB+"] > 15) & (df["Review1"] >= 3) & (df["Review2"] >= 3)])

	elif User == 'O+':
		print(df[["Review1","H.Name"]][(df["O+"] > 15) & (df["Review1"] >= 3) & (df["Review2"] >= 3)])

	elif User == 'A-':
		print(df[["Review1","H.Name" ]][(df["A-"] > 15) & (df["Review1"] >= 3) & (df["Review2"] >= 3)])

	elif User == 'B-':
		print(df[["Review1","H.Name" ]][(df["B-"] > 15) & (df["Review1"] >= 3) & (df["Review2"] >= 3)])

	elif User == 'O-':
		print(df[["Review1","H.Name" ]][(df["O-"] > 15) & (df["Review1"] >= 3) & (df["Review2"] >= 3)])

	elif User == 'AB-':
		print(df[["Review1","H.Name" ]][(df["AB-"] > 15) & (df["Review"] >= 3) & (df["Review2"] >= 3)])

	else:
		print("EXIT")
		break