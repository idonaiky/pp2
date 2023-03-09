import re
file = open("C:/Users/admin/Documents/pp2/5lab/file.txt", "\r")
result = re.sub('(.)([A-Z][a-z]+)', r'\1_\2',file.read()).lower()
print(result)