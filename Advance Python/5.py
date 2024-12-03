"5.Write a Python program to check the current position of the file cursor using tell()."
file_name = 'advc-prg.txt'
file=open(file_name,'w')
file.write('hellow world')

file=open(file_name,'r')
print(file.read(5))
cursor=file.tell()
print(cursor)
