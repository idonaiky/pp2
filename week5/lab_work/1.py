import re
file = open("C:/Users/admin/Documents/pp2/5lab/file.txt", "\r")
result = re.findall(".*a.*b.*", file.read())
print(result)