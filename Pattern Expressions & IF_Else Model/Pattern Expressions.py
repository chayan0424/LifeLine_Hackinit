import pandas
import re

df = pandas.read_csv(r"Book111.csv")
df.head()
type(df)
df.shape
df["H.Name"]
bg=['A+','B+','AB+','O+','O-', 'AB-', 'A-', 'B-' ]
print(bg)

a = str()
for col in df.columns:
	a = a + ' ' + col

c = (re.findall('Review[0-9]*', a))

while True:
	d = '''print(df[["H.Name", "Review1"]]'''

	User = input("\nEnter Blood Group You Want (Press Enter to exit) \t")
	if User == '':
		break

	d = d+'[(df["{}"] > 15)'.format(User)
	for i in c:
		d = d + ' & (df["{}"] > 3)'.format(i)
	d = d+'])'

	eval(d)