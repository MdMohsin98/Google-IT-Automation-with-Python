#!/usr/bin/env python3

import re
with open("the_house_on_henry_street.txt", "r") as file:
	for line in file.readlines():
		pattern = r"[0-9].*[0-9]{4,}"
		result = re.findall(pattern, line)
		if len(result) != 0:
			print(result)
		else:
			continue
