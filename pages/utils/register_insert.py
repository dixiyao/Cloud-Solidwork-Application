import sys
import pandas as pd

df = pd.read_csv(r'/root/inf/user_data.txt')
account, password = sys.argv[1], sys.argv[2]
inf = pd.DataFrame({
	'account': account,
	'password': password,
	'username': 'Undefined',
	'userpassword': 'Undefined',
	'ip': 'Undefined',
}, index=[0])
df = df.append(inf, ignore_index=True)
df.to_csv(r'/root/inf/user_data.txt', index=False)
