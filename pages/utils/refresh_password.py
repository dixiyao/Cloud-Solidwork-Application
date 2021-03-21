import sys
import pandas as pd

file = open(r'/root/tmp/current_userpassword.txt', 'w')
file.write(sys.argv[1])
file.close()

file = open(r'/root/tmp/current_account.txt', 'r')
account = file.read()
file.close()

df = pd.read_csv(r'/root/inf/user_data.txt')
for i in range(len(df)):
	if str(df.iloc[i].account) == account:
		df.iloc[i].userpassword = sys.argv[1]
		break

df.to_csv(r'/root/inf/user_data.txt', index=False)
