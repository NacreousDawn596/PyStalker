from requests import *
from sys import *
try:
	name = argv[1]
except IndexError:
	print('''
	OPTIONS:
			python3 main.py username''')
	exit()
for url in open('data.txt', 'r').read().splitlines():
	try:
		if get(f'{url}{name}').status_code == 200:
			print(f'FOUND: {url}{name}')
		else:
			#print(f'unfound: {url}{name}') in case to make sure that the script is working. 
			pass
	except:
		pass
