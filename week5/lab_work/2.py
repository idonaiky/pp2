import re
file = open("C:/Users/admin/Documents/pp2/5lab/file.txt", "\r")
result = re.findall(r".*a+.*b+.*b+.*b*.*", file.read())
print(result)