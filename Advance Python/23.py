"23) Write a Python program to search for a word in a string using re.search()."
import re

data = "rahul,jina,rajkot,bhavnagar,surat,56,25.32,25/2/95,fgewfsbc@gmail.com,mango,23,sgxyqw,dwdw 23," 
pattern = r'\bmango\b'

res = re.search(pattern,data)

print(res)