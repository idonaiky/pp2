import re
file = open("C:/Users/admin/Documents/pp2/5lab/file.txt", "\r")
result = re.findall("[a-z]+_[a-z]+", file.read())
print(result)