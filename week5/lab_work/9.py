import re
file = open("C:/Users/admin/Documents/pp2/5lab/file.txt", "\r")
result = re.sub(r"(\w)([A-Z])", r"\1 \2", file.read())
print(result)