def pln(a):
     t= a[::-1]
     if t==t[::-1]:
         print('Yes')
     else:
         print('No')
 pln(str(input()))