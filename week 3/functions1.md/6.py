def reverse(string):
     s = string.split()[::-1]
     l = []
     for i in s:
         l.append(i)
     return " ".join(l)
 print(reverse(string))