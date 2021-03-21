import sys
import pandas as pd

df = pd.read_csv(r'/root/inf/user_data.txt')
account = sys.argv[1]
if account in df.account.values:
	f = 0
else:
	f = 1
file = open(r'/root/tmp/tmp_register_check.txt', 'w')
file.write(str(f))
file.close()
