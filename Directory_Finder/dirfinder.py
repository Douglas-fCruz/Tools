#!/usr/bin/env python3

import sys, requests

domain = sys.argv[1]

with open(sys.argv[2], 'r') as directory:
	dirs = directory.read().splitlines()

for dir in dirs:
	url = f"https://{domain}/{dir}"
	try:
		response = requests.get(url)
		if response.status_code == 200:
			print (f"[+] {url}")
	except:
		pass
