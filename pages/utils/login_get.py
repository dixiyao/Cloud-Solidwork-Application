import sys
import pandas as pd

df = pd.read_csv(r'/root/inf/user_data.txt')
account, password = sys.argv[1], sys.argv[2]
f = 0
for i in range(len(df)):
	if str(df.iloc[i].account) == account and str(df.iloc[i].password) == password:
		f = 1
		break

file = open(r'/root/tmp/tmp_login_get.txt', 'w')
file.write(str(f))
file.close()
