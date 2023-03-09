import re
file = open("C:/Users/admin/Documents/pp2/5lab/file.txt", "\r")
result = re.compile(r"[ ,.]",file.read())
print(result)