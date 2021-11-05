from requests import *
from sys import *
try:
	name = argv[1]
except IndexError:
	print('''
	OPTIONS:
			python3 main.py username''')
	exit()
urls = open('data.txt', 'r').read().splitlines()
for url in urls:
	if get(f'{url}{name}').status_code == 200:
		print(f'FOUND: {url}{name}')
	else:
		pass
