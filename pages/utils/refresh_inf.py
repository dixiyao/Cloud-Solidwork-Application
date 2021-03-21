import sys
import pandas as pd

file = open(r'/root/tmp/tmp_address.txt', 'w')
file.write("Undefined")
file.close()

file = open(r'/root/tmp/current_ip.txt', 'w')
file.write("Undefined")
file.close()

file = open(r'/root/tmp/current_username.txt', 'w')
file.write("Undefined")
file.close()

file = open(r'/root/tmp/current_userpassword.txt', 'w')
file.write("Undefined")
file.close()

file = open(r'/root/tmp/current_account.txt', 'r')
account = file.read()
file.close()

df = pd.read_csv(r'/root/inf/user_data.txt')
for i in range(len(df)):
	if str(df.iloc[i].account) == account:
		df.iloc[i].ip = "Undefined"
		df.iloc[i].username = "Undefined"
		df.iloc[i].userpassword = "Undefined"
		break

df.to_csv(r'/root/inf/user_data.txt', index=False)
