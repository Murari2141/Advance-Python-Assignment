"4.Write a Python program to read a file and print the data on the console."

file_name = 'advc-prg.txt'
file=open(file_name,'w')
file.write('hellow world')

file=open(file_name,'r')
print(file.read())
