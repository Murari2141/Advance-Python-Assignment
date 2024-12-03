"24) Write a Python program to match a word in a string using re.match()."

import re

data = "mango,rahfdey,3266,23,sgxyqw,dwdw 23," 
pattern = r'\bmango\b'

res = re.match(pattern,data)

print(res)