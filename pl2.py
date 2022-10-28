import os.path

print(os.path.realpath('.'))

with open('remote-session.info', 'w') as outfile:
	print('Hello World!', file=outfile)


