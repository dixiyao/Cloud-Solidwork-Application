import sys
import pandas as pd

df = pd.read_csv(r'/root/inf/user_data.txt')
account = sys.argv[1]
for i in range(len(df)):
	if str(df.iloc[i].account) == account:
		file = open(r'/root/tmp/current_account.txt', 'w')
		file.write(str(df.iloc[i].account))
		file.close()

		file = open(r'/root/tmp/current_username.txt', 'w')
		file.write(str(df.iloc[i].username))
		file.close()

		file = open(r'/root/tmp/current_userpassword.txt', 'w')
		file.write(str(df.iloc[i].userpassword))
		file.close()

		file = open(r'/root/tmp/current_ip.txt', 'w')
		file.write(str(df.iloc[i].ip))
		file.close()
