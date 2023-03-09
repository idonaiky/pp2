import re
file = open("C:/Users/admin/Documents/pp2/5lab/file.txt", "\r")
result = re.findall('[A-Z][^A-Z]*',file.read())
print(result)
